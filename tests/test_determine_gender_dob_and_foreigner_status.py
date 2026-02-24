import pytest
from datetime import date
from cnp_toolkit.cnp_analysis.determine_gender_dob_foreign import determine_gender_dob_and_foreigner_status


def test_male_1998():
    result = determine_gender_dob_and_foreigner_status("1980408416112")

    assert result.gender == "Male"
    assert result.date_of_birth == date(1998, 4, 8)
    assert result.century_deterministic is True
    assert result.is_foreigner is False


def test_female_2004():
    result = determine_gender_dob_and_foreigner_status("6040703213245")

    assert result.gender == "Female"
    assert result.date_of_birth == date(2004, 7, 3)
    assert result.century_deterministic is True
    assert result.is_foreigner is False


def test_foreigner_century_not_deterministic():
    result = determine_gender_dob_and_foreigner_status("7800407236210")

    assert result.gender == "Male"
    assert result.date_of_birth == date(1980, 4, 7)  # 1900 prefix assumption
    assert result.century_deterministic is False
    assert result.is_foreigner is True
    
def test_invalid_length():
    with pytest.raises(ValueError):
        determine_gender_dob_and_foreigner_status("123")


def test_non_numeric():
    with pytest.raises(ValueError):
        determine_gender_dob_and_foreigner_status("ABCDEFGHIJKLM")