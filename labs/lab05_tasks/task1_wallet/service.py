from decimal import Decimal, InvalidOperation
import re
from typing import Optional

from .exceptions import (
    BlockedWalletError,
    DuplicateError,
    InsufficientBalanceError,
    NotFoundError,
    ValidationError,
)
from .models import Transaction, TransactionType, Wallet, WalletStatus


class WalletService:
    """Business logic for the digital wallet system."""

    def __init__(self) -> None:
        self.wallets: dict[str, Wallet] = {}
        self._user_to_wallet: dict[str, str] = {}
        self._transaction_counter = 0

    @staticmethod
    def _required_text(value: str, field_name: str) -> str:
        value = str(value).strip()
        if not value:
            raise ValidationError(f"{field_name} cannot be empty.")
        return value

    @staticmethod
    def parse_amount(value) -> Decimal:
        try:
            amount = Decimal(str(value).strip())
        except (InvalidOperation, ValueError, AttributeError):
            raise ValidationError("Amount must be a valid number.")
        if not amount.is_finite():
            raise ValidationError("Amount must be a finite number.")
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount.quantize(Decimal("0.01"))

    @staticmethod
    def validate_mobile(mobile: str) -> str:
        mobile = str(mobile).strip()
        if not re.fullmatch(r"[0-9]{10}", mobile):
            raise ValidationError("Mobile number must contain exactly 10 digits.")
        return mobile

    def _new_transaction_id(self) -> str:
        self._transaction_counter += 1
        return f"TXN{self._transaction_counter:04d}"

    def _get(self, wallet_id: str) -> Wallet:
        wallet_id = str(wallet_id).strip()
        if wallet_id not in self.wallets:
            raise NotFoundError(f"Wallet '{wallet_id}' not found.")
        return self.wallets[wallet_id]

    @staticmethod
    def _ensure_active(wallet: Wallet) -> None:
        if wallet.status == WalletStatus.BLOCKED:
            raise BlockedWalletError(f"Wallet '{wallet.wallet_id}' is blocked.")

    def create_wallet(self, user_id: str, user_name: str, wallet_id: str, mobile_number: str) -> Wallet:
        user_id = self._required_text(user_id, "User ID")
        user_name = self._required_text(user_name, "User name")
        wallet_id = self._required_text(wallet_id, "Wallet ID")
        mobile_number = self.validate_mobile(mobile_number)
        if user_id in self._user_to_wallet:
            raise DuplicateError(f"User ID '{user_id}' already exists.")
        if wallet_id in self.wallets:
            raise DuplicateError(f"Wallet ID '{wallet_id}' already exists.")
        wallet = Wallet(user_id, user_name, wallet_id, mobile_number)
        self.wallets[wallet_id] = wallet
        self._user_to_wallet[user_id] = wallet_id
        return wallet

    def list_wallets(self) -> list[Wallet]:
        return list(self.wallets.values())

    def search_wallet(self, wallet_id: str) -> Wallet:
        return self._get(wallet_id)

    def add_money(self, wallet_id: str, amount) -> Transaction:
        wallet = self._get(wallet_id)
        self._ensure_active(wallet)
        amount = self.parse_amount(amount)
        wallet.balance += amount
        tx = Transaction(self._new_transaction_id(), TransactionType.DEPOSIT, None, wallet.wallet_id, amount, wallet.balance)
        wallet.transaction_history.append(tx)
        return tx

    def withdraw_money(self, wallet_id: str, amount) -> Transaction:
        wallet = self._get(wallet_id)
        self._ensure_active(wallet)
        amount = self.parse_amount(amount)
        if amount > wallet.balance:
            raise InsufficientBalanceError("Insufficient wallet balance.")
        wallet.balance -= amount
        tx = Transaction(self._new_transaction_id(), TransactionType.WITHDRAWAL, wallet.wallet_id, None, amount, wallet.balance)
        wallet.transaction_history.append(tx)
        return tx

    def transfer_money(self, source_id: str, destination_id: str, amount) -> tuple[Transaction, Transaction]:
        source = self._get(source_id)
        destination = self._get(destination_id)
        if source.wallet_id == destination.wallet_id:
            raise ValidationError("Transfer source and destination must be different wallets.")
        self._ensure_active(source)
        self._ensure_active(destination)
        amount = self.parse_amount(amount)
        if amount > source.balance:
            raise InsufficientBalanceError("Insufficient wallet balance for transfer.")

        source.balance -= amount
        destination.balance += amount
        tx_id = self._new_transaction_id()
        source_tx = Transaction(tx_id, TransactionType.TRANSFER, source.wallet_id, destination.wallet_id, amount, source.balance)
        destination_tx = Transaction(tx_id, TransactionType.TRANSFER, source.wallet_id, destination.wallet_id, amount, destination.balance)
        source.transaction_history.append(source_tx)
        destination.transaction_history.append(destination_tx)
        return source_tx, destination_tx

    def current_balance(self, wallet_id: str) -> Decimal:
        return self._get(wallet_id).balance

    def transaction_history(self, wallet_id: str) -> list[Transaction]:
        return list(self._get(wallet_id).transaction_history)

    def set_blocked(self, wallet_id: str, blocked: bool) -> Wallet:
        wallet = self._get(wallet_id)
        wallet.status = WalletStatus.BLOCKED if blocked else WalletStatus.ACTIVE
        return wallet

    def toggle_block(self, wallet_id: str) -> Wallet:
        wallet = self._get(wallet_id)
        wallet.status = WalletStatus.ACTIVE if wallet.status == WalletStatus.BLOCKED else WalletStatus.BLOCKED
        return wallet

    def transaction_summary(self) -> dict:
        transactions = []
        seen = set()
        for wallet in self.wallets.values():
            for tx in wallet.transaction_history:
                if tx.transaction_id not in seen:
                    seen.add(tx.transaction_id)
                    transactions.append(tx)
        deposits = sum((t.amount for t in transactions if t.transaction_type == TransactionType.DEPOSIT), Decimal("0"))
        withdrawals = sum((t.amount for t in transactions if t.transaction_type == TransactionType.WITHDRAWAL), Decimal("0"))
        transfers = sum((t.amount for t in transactions if t.transaction_type == TransactionType.TRANSFER), Decimal("0"))
        return {
            "total_transactions": len(transactions),
            "deposits": deposits,
            "withdrawals": withdrawals,
            "transfers": transfers,
            "total_wallets": len(self.wallets),
        }
