import pytest
from cnp_toolkit.cnp_analysis.analyze_cnp import analyze_cnp

def test_valid_values():
    # Male, Foreigner, December 21st, 1989, Bucharest Sector 1, Code 001
    result = analyze_cnp("7891221410013")# "Male", True, date(1989, 12, 21), , "001"
    assert result.gender == "Male"
    assert result.date_of_birth.year == 1989
    assert result.date_of_birth.month == 12
    assert result.date_of_birth.day == 21
    assert result.is_foreigner == True
    assert result.century_deterministic == False
    assert result.issuing_county == "București - Sector 1"
    assert result.unique_code == "001"
    assert result.is_unique_code_valid == True
    assert result.found_checksum == 3
    assert result.calculated_checksum == 3
    assert result.is_cnp_checksum_valid == True
    #assert analyze_cnp("Female", False, date(2008, 9, 15), "23", "999") == "6080915239997"

#def test_invalid_nnn():
#    with pytest.raises(ValueError):
#        generate_cnp("Male", False, date(1990, 1, 1), "01", "12A")
#    with pytest.raises(ValueError):
#        generate_cnp("Male", False, date(1990, 1, 1), "01", "000")