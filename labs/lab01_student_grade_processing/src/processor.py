MAX_PROJECT = 20
MAX_MINOR = 20
MAX_LAB = 20
MAX_END = 40


def parse_mark(value):
    if value is None or value == "":
        raise ValueError("Missing input")
    if isinstance(value, bool):
        raise ValueError("Invalid data type")
    try:
        if isinstance(value, str) and value.strip() == "":
            raise ValueError("Missing input")
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError("Invalid data type")
    if not number.is_integer():
        raise ValueError("Invalid data type")
    return int(number)


def validate_row(project, minor, lab, end_exam):
    p = parse_mark(project)
    m = parse_mark(minor)
    l = parse_mark(lab)
    e = parse_mark(end_exam)

    if not (0 <= p <= MAX_PROJECT):
        raise ValueError("Project marks out of range")
    if not (0 <= m <= MAX_MINOR):
        raise ValueError("Minor marks out of range")
    if not (0 <= l <= MAX_LAB):
        raise ValueError("Laboratory marks out of range")
    if not (0 <= e <= MAX_END):
        raise ValueError("End examination marks out of range")

    total = p + m + l + e
    if total > 100:
        raise ValueError("Total marks cannot exceed 100")
    return total


def grade_from_total(total):
    if total < 0 or total > 100:
        raise ValueError("Total marks must be between 0 and 100")
    if total >= 90:
        return "A"
    if total >= 75:
        return "B"
    if total >= 60:
        return "C"
    if total >= 35:
        return "D"
    return "F"
