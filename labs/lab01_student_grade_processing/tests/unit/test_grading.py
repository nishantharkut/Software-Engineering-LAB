import pytest

from labs.lab01_student_grade_processing.src.processor import grade_from_total


@pytest.mark.parametrize(
    "marks, expected",
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (75, "B"),
        (74, "C"),
        (60, "C"),
        (59, "D"),
        (35, "D"),
        (34, "F"),
        (0, "F"),
    ],
)
def test_grade_from_total(marks, expected):
    assert grade_from_total(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_grade_from_total_rejects_totals_outside_valid_range(marks):
    with pytest.raises(ValueError, match="Total marks must be between 0 and 100"):
        grade_from_total(marks)
