from ..utilities.constants import COUNTY_CODES

def get_county_code(county_name: str) -> str:
    """Get county code from name

    Args:
        county_name (str): The name of the county

    Raises:
        ValueError: If input name doesn't exist.

    Returns:
        str: The county code
    """
    
    # If input is already a valid code, return it (and validate it exists)
    if county_name in {v for v in COUNTY_CODES.values()}:
        return county_name

    # If input is a valid county name -> Return corresponding code
    if county_name in COUNTY_CODES:
        return COUNTY_CODES[county_name]

    # Else -> Provided name is not valid, raise error
    raise ValueError(f"Invalid county input: {county_name}")
