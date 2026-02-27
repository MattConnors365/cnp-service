from ..exceptions import CNPInvalidLengthError, CNPInvalidCharacterError
from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class CNPAnalysisGenderAndDate:
    gender: Literal["Unknown", "Male", "Female"]
    date_of_birth: date
    century_deterministic: bool
    is_foreigner: bool

def determine_gender_dob_and_foreigner_status(cnp: str) -> CNPAnalysisGenderAndDate:
    """Determines the gender, date of birth, and foreigner status of a CNP
    IMPORTANT: If the CNP belongs to a foreigner, the field century_deterministic will be set to False,
    as it is impossible to decode the century for foreign CNPs.
    If is_foreigner == True, the program will make the presumption that the century is the 1900s;
    This is simply to avoid hard crashes, please check if the century is deterministic. If it isn't, it means the program simply used the most likely century.
    IMPORTANT: If the first digit is 9, not only will century_deterministic = False and is_foreigner = True,
    but also gender = "Unknown" because that digit encodes for neither gender nor century

    Args:
        cnp (str): 13-digit string

    Raises:
        CNPInvalidLengthError: If CNP is not a 13 character string
        CNPInvalidCharacterError: If CNP contains non-digit characters
        ValueError: If the first digit is invalid
    Returns:
        CNPAnalysisGenderAndDate: DataClass that holds previously mentioned fields: gender, date_of_birth, is_foreigner, century_deterministic
    """

    if not len(cnp) == 13:
        raise CNPInvalidLengthError()
    if not cnp.isdigit():
        raise CNPInvalidCharacterError()

    s = int(cnp[0])
    yy = int(cnp[1:3])
    mm = int(cnp[3:5])
    dd = int(cnp[5:7])

    # Determine gender
    if s == 9:
        gender = "Unknown"
    else:
        gender = "Female" if s % 2 == 0 else "Male"

    # Determine century + foreigner status
    century_deterministic = True
    is_foreigner = False

    if s in (1, 2):
        century = 1900
    elif s in (3, 4):
        century = 1800
    elif s in (5, 6):
        century = 2000
    elif s in (7, 8, 9):
        century = 1900  # placeholder assumption
        is_foreigner = True
        century_deterministic = False
    else:
        raise ValueError("Invalid first digit in CNP")

    year = century + yy
    dob = date(year, mm, dd)

    return CNPAnalysisGenderAndDate(
        gender=gender,
        date_of_birth=dob,
        century_deterministic=century_deterministic,
        is_foreigner=is_foreigner,
    )