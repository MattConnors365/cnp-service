import pytest
from cnp_toolkit.cnp_analysis.get_county_name import get_county_name

def test_valid_codes():
    # Input is a code, should return the county name
    assert get_county_name("01") == "Alba"
    assert get_county_name("45") == "București - Sector 5"
    # Universal code name
    assert get_county_name("70") == "Universal / New system"

def test_invalid_inputs():
    # Nonexistent codes
    with pytest.raises(ValueError):
        get_county_name("99")
    # Empty string
    with pytest.raises(ValueError):
        get_county_name("")

def test_case_sensitivity():
    # Should be case-sensitive
    with pytest.raises(ValueError):
        get_county_name("alba")  # lowercase not valid
