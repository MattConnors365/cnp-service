from datetime import date
from typing import Literal, Optional
from .first_digit import first_digit
from .generate_date_of_birth_sequence import generate_date_of_birth_sequence
from .get_county_code import get_county_code
from .generate_unique_code import generate_unique_code
from ..checksum import generate_checksum

def generate_cnp(
    gender: Literal["Male", "Female"],
    is_foreigner: bool,
    dob: date,
    county: str,
    nnn: Optional[str] = None
) -> str:
    """Generates a CNP based on inputs

    Args:
        gender (Literal[&quot;Male&quot;, &quot;Female&quot;]): Legal gender
        is_foreigner (bool): True if born outside Romania
        dob (date): Date of birth
        county (str): County name or code (see official CNP JJ codes)
        nnn (Optional[str], optional): If you already thought of a unique code. Defaults to None.

    Raises:
        TypeError: If provided NNN isn't a string
        ValueError: If provided NNN isn't 3 digits long
        ValueError: If provided NNN isn't in the range 001-999

    Returns:
        str: 13-digit long numeric string
    """
    digit_one = str(first_digit(gender, dob.year, is_foreigner))
    dob_sequence = generate_date_of_birth_sequence(dob.year, dob.month, dob.day)
    county_code = get_county_code(county)
    if nnn is None:
        nnn = generate_unique_code()
    else:
        if not isinstance(nnn, str):
            raise TypeError("NNN must be a string.")
        elif not (nnn.isdigit() and len(nnn) == 3):
            raise ValueError("NNN must be 3 digits long.")
        elif int(nnn) not in range(1, 1000):
            raise ValueError("NNN must be between 001-999")
    partial = f"{digit_one}{dob_sequence}{county_code}{nnn}"
    c = generate_checksum(partial)
    return f"{partial}{c}"