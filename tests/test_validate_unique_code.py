import pytest
from cnp_toolkit.cnp_analysis.validate_unique_code import validate_unique_code

def test_valid_unique_codes():
    assert validate_unique_code("1234567890012")  # 001 valid
    assert validate_unique_code("1234567899992")  # 999 valid

def test_invalid_unique_codes():
    assert not validate_unique_code("1234567890002")  # 000 invalid
    assert not validate_unique_code("123456789ABC2")  # non-digit
    assert not validate_unique_code("123")            # too short