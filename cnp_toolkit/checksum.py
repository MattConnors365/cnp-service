from .exceptions import CNPInvalidLengthError, CNPInvalidCharacterError

CONSTANT: tuple[int, ...] = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)

def generate_checksum(unfinished_cnp: str) -> int:
    """Generate checksum for a 12-digit CNP prefix.

    Args:
        unfinished_cnp (str): A 12-character long string; the CNP without an existing checksum

    Raises:
        CNPInvalidLengthError: if the input isn't 12 characters long
        CNPInvalidCharacterError: if the input contains any character other than arabic numerals

    Returns:
        int: 1-digit checksum
    """
    
    # Validation
    
    if len(unfinished_cnp) != 12:
        raise CNPInvalidLengthError(
            f"Invalid length: {len(unfinished_cnp)}. Must be exactly 12 characters long."
        )

    if not unfinished_cnp.isdigit():
        raise CNPInvalidCharacterError()

    # Logic

    total = sum(
        int(digit) * multiplier
        for digit, multiplier in zip(unfinished_cnp, CONSTANT)
    )

    remainder = total % 11

    return 1 if remainder == 10 else remainder