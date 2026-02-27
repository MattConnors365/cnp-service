from typing import Literal

def first_digit(legal_gender: Literal["Male", "Female"], year_of_birth: int, is_foreigner: bool) -> int:
    """
    Combines legal gender, year of birth, and foreigner status to generate
    the first digit of a Romanian CNP.

    Rules:
    - Male: base 1, Female: base 2
    - If the person is a foreigner, add 6 to the base digit.
    - If not a foreigner, the second digit of the year determines an addition:
        - '8' -> +2
        - '0' -> +4
        - '9' -> +0

    Args:
        legal_gender (str): "Male" or "Female".
        year_of_birth (int): 4-digit year between 1800 and 2099.
        is_foreigner (bool): True if born outside Romania.

    Raises:
        TypeError: If input types are incorrect
        ValueError: If values out of range.

    Returns:
        int: The 1-digit number encoding gender, century, and foreigner status.
    """

    # Validation

    if not isinstance(legal_gender, str):
        raise TypeError(f"legal_gender must be a string, not {type(legal_gender).__name__}.")
    if not isinstance(year_of_birth, int):
        raise TypeError(f"year_of_birth must be an integer, not {type(year_of_birth).__name__}.")
    if not isinstance(is_foreigner, bool):
        raise TypeError(f"is_foreigner must be a boolean, not {type(is_foreigner).__name__}.")

    if legal_gender not in ("Male", "Female"):
        raise ValueError("legal_gender must be 'Male' or 'Female'.")
    if not (1800 <= year_of_birth <= 2099):
        raise ValueError("year_of_birth must be between 1800 and 2099.")

    # Base digit
    digit = 1 if legal_gender == "Male" else 2

    # Foreigner adjustment
    if is_foreigner:
        digit += 6
    else:
        year_str = str(year_of_birth)
        second_digit = year_str[1]
        if second_digit == '8':
            digit += 2
        elif second_digit == '0':
            digit += 4
        elif second_digit == '9':
            digit += 0

    return digit