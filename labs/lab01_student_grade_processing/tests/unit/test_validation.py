import pytest

from labs.lab01_student_grade_processing.src.processor import parse_mark, validate_row

@pytest.mark.parametrize(
    "value",
    [None, "", "   ", "AB", "Absent", 20.5, True],
)
def test_parse_mark_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_mark(value)


def test_validate_row_rejects_total_over_limit():
    with pytest.raises(ValueError, match="End examination marks out of range"):
        validate_row(20, 20, 20, 41)


def test_validate_row_rejects_missing_input():
    with pytest.raises(ValueError, match="Missing input"):
        validate_row(17, None, 18, 36)


def test_validate_row_rejects_text_input():
    with pytest.raises(ValueError, match="Invalid data type"):
        validate_row(15, "AB", 16, 30)
