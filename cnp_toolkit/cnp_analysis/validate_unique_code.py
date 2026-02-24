

def validate_unique_code(cnp: str) -> bool:
    """Validates a given CNP's unique code

    Args:
        cnp (str): 13-digit numeric string

    Returns:
        bool: True if the unique code is valid (3 digits in the range 001-999), False otherwise
    """

    seq = cnp[9:12]
    return seq.isdigit() and 1 <= int(seq) <= 999