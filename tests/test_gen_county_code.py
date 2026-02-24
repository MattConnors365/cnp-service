import pytest
from cnp_toolkit.cnp_generation.get_county_code import get_county_code
from cnp_toolkit.utilities.constants import COUNTY_CODES

def test_valid_names():
    # Regular counties
    assert get_county_code("Alba") == "01"
    assert get_county_code("București - Sector 5") == "45"
    # Universal code name
    assert get_county_code("Universal / New system") == "70"

def test_valid_codes():
    # Input is already a code
    assert get_county_code("01") == "01"
    assert get_county_code("45") == "45"
    assert get_county_code("70") == "70"

def test_invalid_inputs():
    # Completely wrong names
    with pytest.raises(ValueError):
        get_county_code("Atlantis")
    # Nonexistent codes
    with pytest.raises(ValueError):
        get_county_code("99")
    # Empty string
    with pytest.raises(ValueError):
        get_county_code("")

def test_case_sensitivity():
    # Should be case-sensitive
    with pytest.raises(ValueError):
        get_county_code("alba")  # lowercase not valid
