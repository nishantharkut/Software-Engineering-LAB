"""Unit tests for book status determination."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.processor import determine_status


@pytest.mark.parametrize("copies", [1, 2, 5, 10, 100])
def test_determine_status_returns_available_when_copies_greater_than_zero(copies):
    """When available copies > 0, status should be 'Available'."""
    assert determine_status(copies) == "Available"


def test_determine_status_returns_issued_out_when_zero_copies():
    """When available copies = 0, status should be 'Issued Out'."""
    assert determine_status(0) == "Issued Out"


def test_determine_status_rejects_negative_copies():
    """Negative available copies should raise ValueError."""
    with pytest.raises(ValueError, match="Negative available copies"):
        determine_status(-1)