from datetime import date

def generate_date_of_birth_sequence(year: int, month: int, day: int) -> str:
    """
    Generates a 6-digit sequence (YYMMDD) from year, month, and day integers.
    
    Args:
        year (int): Year (1800-2099)
        month (int): Month (1-12)
        day (int): Day (1-31)
        
    Returns:
        str: 6-digit string representation 'YYMMDD'
    """
    # Validation
    
    if not (1800 <= year <= 2099):
        raise ValueError(f"Year {year} is outside the valid CNP range (1800-2099).")

    try:
        dob = date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")

    # Generation
    
    return dob.strftime("%y%m%d")
