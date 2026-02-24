import pytest
from cnp_toolkit.cnp_generation.generate_cnp import generate_cnp
from datetime import date

def test_valid_values():
    assert generate_cnp("Male", True, date(1989, 12, 21), "București - Sector 1", "001") == "7891221410013"
    assert generate_cnp("Female", False, date(2008, 9, 15), "23", "999") == "6080915239997"

def test_invalid_nnn():
    with pytest.raises(ValueError):
        generate_cnp("Male", False, date(1990, 1, 1), "01", "12A")
    with pytest.raises(ValueError):
        generate_cnp("Male", False, date(1990, 1, 1), "01", "000")