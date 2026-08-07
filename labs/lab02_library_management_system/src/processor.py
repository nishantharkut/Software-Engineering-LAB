def parse_copies(value):
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
    count = int(number)
    if count < 0:
        raise ValueError("Negative inventory value")
    return count


def validate_book_record(total_copies, available_copies, issued_copies):
    total = parse_copies(total_copies)
    available = parse_copies(available_copies)
    issued = parse_copies(issued_copies)

    if total != available + issued:
        raise ValueError(
            f"Total copies ({total}) does not equal "
            f"available ({available}) + issued ({issued})"
        )
    return available


def determine_status(available_copies):
    if available_copies < 0:
        raise ValueError("Negative available copies")
    if available_copies == 0:
        return "Issued Out"
    return "Available"