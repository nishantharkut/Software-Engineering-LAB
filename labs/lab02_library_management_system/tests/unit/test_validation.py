"""Unit tests for library book record validation."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.processor import parse_copies, validate_book_record


@pytest.mark.parametrize(
    "value",
    [None, "", "   ", "Five", "AB", 3.5, True],
)
def test_parse_copies_rejects_invalid_values(value):
    """Invalid values should raise ValueError."""
    with pytest.raises(ValueError):
        parse_copies(value)


def test_parse_copies_rejects_negative():
    """Negative values should raise ValueError."""
    with pytest.raises(ValueError, match="Negative inventory value"):
        parse_copies(-2)


def test_parse_copies_accepts_valid_integers():
    """Valid integer values should be parsed correctly."""
    assert parse_copies(10) == 10
    assert parse_copies(0) == 0
    assert parse_copies("5") == 5
    assert parse_copies(7.0) == 7


def test_validate_book_record_rejects_constraint_violation():
    """Records where total != available + issued should raise ValueError."""
    with pytest.raises(ValueError, match="does not equal"):
        validate_book_record(10, 7, 5)


def test_validate_book_record_rejects_missing_input():
    """Records with missing values should raise ValueError."""
    with pytest.raises(ValueError, match="Missing input"):
        validate_book_record(10, None, 5)


def test_validate_book_record_rejects_text_input():
    """Records with text instead of numbers should raise ValueError."""
    with pytest.raises(ValueError, match="Invalid data type"):
        validate_book_record(10, "Five", 5)


def test_validate_book_record_rejects_negative_inventory():
    """Records with negative values should raise ValueError."""
    with pytest.raises(ValueError, match="Negative inventory value"):
        validate_book_record(10, -2, 12)


def test_validate_book_record_returns_available_on_success():
    """Valid records should return the available copies count."""
    available = validate_book_record(10, 7, 3)
    assert available == 7


def test_validate_book_record_accepts_zero_available():
    """Records with zero available copies should be valid."""
    available = validate_book_record(5, 0, 5)
    assert available == 0