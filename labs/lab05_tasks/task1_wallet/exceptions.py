class WalletError(Exception):
    """Base class for wallet application errors."""


class ValidationError(WalletError):
    """Raised when input violates a validation rule."""


class DuplicateError(WalletError):
    """Raised when a unique identifier already exists."""


class NotFoundError(WalletError):
    """Raised when a wallet cannot be found."""


class InsufficientBalanceError(WalletError):
    """Raised when a withdrawal/transfer exceeds the balance."""


class BlockedWalletError(WalletError):
    """Raised when an operation involves a blocked wallet."""
