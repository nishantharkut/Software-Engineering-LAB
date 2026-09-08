from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional


class WalletStatus(str, Enum):
    ACTIVE = "Active"
    BLOCKED = "Blocked"


class TransactionType(str, Enum):
    DEPOSIT = "Deposit"
    WITHDRAWAL = "Withdrawal"
    TRANSFER = "Transfer"


@dataclass(frozen=True)
class Transaction:
    transaction_id: str
    transaction_type: TransactionType
    source_wallet: Optional[str]
    destination_wallet: Optional[str]
    amount: Decimal
    updated_balance: Decimal


@dataclass
class Wallet:
    user_id: str
    user_name: str
    wallet_id: str
    mobile_number: str
    balance: Decimal = Decimal("0.00")
    status: WalletStatus = WalletStatus.ACTIVE
    transaction_history: list[Transaction] = field(default_factory=list)
