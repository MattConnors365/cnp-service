from ..utilities.constants import CODES_TO_COUNTIES

def get_county_name(county_code: str) -> str:
    """Get county name from code

    Args:
        county_code (str): The code of the county

    Raises:
        ValueError: If input code doesn't exist.

    Returns:
        str: The county name
    """
    
    # If input is a valid county code -> Return corresponding name
    if county_code in CODES_TO_COUNTIES:
        return CODES_TO_COUNTIES[county_code]

    # Else -> Provided code is not valid, raise error
    raise ValueError(f"Invalid county code: {county_code}")
