from ..exceptions import CNPInvalidDateError
from datetime import date

def generate_date_of_birth_sequence(year: int, month: int, day: int) -> str:
    """
    Generates a 6-digit sequence (YYMMDD) from year, month, and day integers.
    
    Args:
        year (int): Year (1800-2099)
        month (int): Month (1-12)
        day (int): Day (1-31)

    Raises:
        CNPInvalidDateError: If the date is out of range.

    Returns:
        str: 6-digit string representation 'YYMMDD'
    """
    if not (1800 <= year <= 2099):
        raise CNPInvalidDateError(f"Year {year} is outside the valid CNP range (1800-2099).")

    try:
        dob = date(year, month, day)
    except (ValueError, TypeError) as e:
        raise CNPInvalidDateError(f"Invalid date components: {e}")

    return dob.strftime("%y%m%d")
