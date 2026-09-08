from decimal import Decimal
import pytest

from task1_wallet.exceptions import BlockedWalletError, DuplicateError, InsufficientBalanceError, NotFoundError, ValidationError
from task1_wallet.models import TransactionType, WalletStatus
from task1_wallet.service import WalletService


def wallet_service():
    s = WalletService()
    s.create_wallet("U1", "Alice", "W1", "9876543210")
    s.create_wallet("U2", "Bob", "W2", "9123456780")
    return s


def test_valid_record_creation():
    s = WalletService()
    w = s.create_wallet("U1", "Alice", "W1", "9876543210")
    assert w.wallet_id == "W1" and w.balance == Decimal("0.00")


def test_duplicate_user_id_rejected():
    s = wallet_service()
    with pytest.raises(DuplicateError): s.create_wallet("U1", "Other", "W3", "9000000000")


def test_duplicate_wallet_id_rejected():
    s = wallet_service()
    with pytest.raises(DuplicateError): s.create_wallet("U3", "Other", "W1", "9000000000")


def test_wallet_not_found():
    with pytest.raises(NotFoundError): wallet_service().search_wallet("W404")


def test_empty_name_rejected():
    with pytest.raises(ValidationError): WalletService().create_wallet("U1", "   ", "W1", "9876543210")


def test_invalid_mobile_rejected():
    with pytest.raises(ValidationError): WalletService().create_wallet("U1", "Alice", "W1", "12345")


def test_invalid_numerical_deposit_rejected():
    with pytest.raises(ValidationError): wallet_service().add_money("W1", "abc")


@pytest.mark.parametrize("amount", [0, -1, "0", "-25"])
def test_non_positive_deposit_rejected(amount):
    with pytest.raises(ValidationError): wallet_service().add_money("W1", amount)


def test_valid_deposit_updates_balance_and_history():
    s = wallet_service()
    tx = s.add_money("W1", "100.00")
    assert s.current_balance("W1") == Decimal("100.00")
    assert tx.transaction_type == TransactionType.DEPOSIT
    assert tx.updated_balance == Decimal("100.00")


def test_insufficient_withdrawal_rejected():
    with pytest.raises(InsufficientBalanceError): wallet_service().withdraw_money("W1", 1)


def test_valid_withdrawal_updates_balance():
    s = wallet_service(); s.add_money("W1", 100)
    tx = s.withdraw_money("W1", 40)
    assert tx.transaction_type == TransactionType.WITHDRAWAL
    assert s.current_balance("W1") == Decimal("60.00")


def test_transfer_to_non_existing_wallet_rejected():
    with pytest.raises(NotFoundError): wallet_service().transfer_money("W1", "W404", 10)


def test_transfer_to_same_wallet_rejected():
    with pytest.raises(ValidationError): wallet_service().transfer_money("W1", "W1", 10)


def test_blocked_wallet_rejects_transaction():
    s = wallet_service(); s.set_blocked("W1", True)
    assert s.search_wallet("W1").status == WalletStatus.BLOCKED
    with pytest.raises(BlockedWalletError): s.add_money("W1", 10)


def test_transfer_involving_blocked_destination_rejected_without_balance_change():
    s = wallet_service(); s.add_money("W1", 100); s.set_blocked("W2", True)
    with pytest.raises(BlockedWalletError): s.transfer_money("W1", "W2", 20)
    assert s.current_balance("W1") == Decimal("100.00")
    assert s.current_balance("W2") == Decimal("0.00")


def test_transfer_success_updates_both_wallets_and_history():
    s = wallet_service(); s.add_money("W1", 100)
    source_tx, dest_tx = s.transfer_money("W1", "W2", 35)
    assert s.current_balance("W1") == Decimal("65.00")
    assert s.current_balance("W2") == Decimal("35.00")
    assert source_tx.transaction_id == dest_tx.transaction_id
    assert len(s.transaction_history("W1")) == 2
    assert len(s.transaction_history("W2")) == 1


def test_balance_never_becomes_negative():
    s = wallet_service(); s.add_money("W1", 10)
    with pytest.raises(InsufficientBalanceError): s.withdraw_money("W1", 10.01)
    assert s.current_balance("W1") == Decimal("10.00")


def test_toggle_block_unblock():
    s = wallet_service(); s.toggle_block("W1"); assert s.search_wallet("W1").status == WalletStatus.BLOCKED
    s.toggle_block("W1"); assert s.search_wallet("W1").status == WalletStatus.ACTIVE


def test_transaction_summary_counts_unique_transactions():
    s = wallet_service(); s.add_money("W1", 100); s.withdraw_money("W1", 20); s.transfer_money("W1", "W2", 30)
    summary = s.transaction_summary()
    assert summary == {"total_transactions": 3, "deposits": Decimal("100.00"), "withdrawals": Decimal("20.00"), "transfers": Decimal("30.00"), "total_wallets": 2}
