import pytest
from cnp_toolkit.cnp_generation.first_digit import first_digit  # adjust import path if needed

def test_first_digit_regular():
    # Male, non-foreigner, year 1985 → second digit '9' → +0
    assert first_digit("Male", 1985, False) == 1
    # Female, non-foreigner, year 2000 → second digit '0' → +4
    assert first_digit("Female", 2000, False) == 6
    # Male, non-foreigner, year 1898 → second digit '8' → +2
    assert first_digit("Male", 1898, False) == 3

def test_first_digit_foreigner():
    # Male, foreigner → base 1 + 6
    assert first_digit("Male", 1990, True) == 7
    # Female, foreigner → base 2 + 6
    assert first_digit("Female", 1985, True) == 8

def test_first_digit_invalid_inputs():
    # Wrong gender
    with pytest.raises(ValueError):
        first_digit("Unknown", 1990, False)
    # Year out of range
    with pytest.raises(ValueError):
        first_digit("Male", 1700, False)
    with pytest.raises(ValueError):
        first_digit("Male", 2100, False)
    # Wrong types
    with pytest.raises(TypeError):
        first_digit(123, 1990, False)
    with pytest.raises(TypeError):
        first_digit("Male", "1990", False)
    with pytest.raises(TypeError):
        first_digit("Male", 1990, "nope")