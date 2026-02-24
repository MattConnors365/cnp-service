from .determine_gender_dob_foreign import determine_gender_dob_and_foreigner_status
from .get_county_name import get_county_name
from .validate_unique_code import validate_unique_code
from ..checksum import generate_checksum
from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class CNPAnalysis:
    gender: Literal["Unknown", "Male", "Female"]
    date_of_birth: date
    century_deterministic: bool
    is_foreigner: bool
    issuing_county: str
    unique_code: str
    is_unique_code_valid: bool
    found_checksum: int
    calculated_checksum: int
    is_cnp_checksum_valid: bool

def analyze_cnp(cnp: str) -> CNPAnalysis:
    """Analyzes a given CNP

    Args:
        cnp (str): 13-digit numeric string

    Raises:
        ValueError: If CNP is not a 13-digit numeric string

    Returns:
        CNPAnalysis: Data extracted from the analysis
    """
    if not (cnp.isdigit() and len(cnp) == 13):
        raise ValueError("CNP must be a 13-digit string")

    # 1. Gender, DOB, century, foreigner
    gender_dob = determine_gender_dob_and_foreigner_status(cnp)

    # 2. County
    issuing_county = get_county_name(cnp[7:9])

    # 3. Unique code
    unique_code = cnp[9:12]
    is_unique_code_valid = validate_unique_code(cnp)

    # 4. Checksum
    expected_checksum = int(cnp[-1])
    actual_checksum = generate_checksum(cnp[:-1])
    is_cnp_checksum_valid = (expected_checksum == actual_checksum)

    return CNPAnalysis(
        gender=gender_dob.gender,
        date_of_birth=gender_dob.date_of_birth,
        century_deterministic=gender_dob.century_deterministic,
        is_foreigner=gender_dob.is_foreigner,
        issuing_county=issuing_county,
        unique_code=unique_code,
        is_unique_code_valid=is_unique_code_valid,
        found_checksum=expected_checksum,
        calculated_checksum=actual_checksum,
        is_cnp_checksum_valid=is_cnp_checksum_valid
    )