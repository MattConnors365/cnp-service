import pytest
from cnp_toolkit.cnp_generation.generate_date_of_birth_sequence import generate_date_of_birth_sequence

def test_valid_dates():
    # Typical date
    assert generate_date_of_birth_sequence(2005, 3, 25) == "050325"
    # Leap year
    assert generate_date_of_birth_sequence(2000, 2, 29) == "000229"
    # Boundary year
    assert generate_date_of_birth_sequence(1800, 1, 1) == "000101"
    assert generate_date_of_birth_sequence(2099, 12, 31) == "991231"

def test_invalid_year():
    with pytest.raises(ValueError):
        generate_date_of_birth_sequence(1799, 1, 1)
    with pytest.raises(ValueError):
        generate_date_of_birth_sequence(2100, 1, 1)

def test_invalid_month_day():
    # Invalid month
    with pytest.raises(ValueError):
        generate_date_of_birth_sequence(2000, 13, 1)
    # Invalid day
    with pytest.raises(ValueError):
        generate_date_of_birth_sequence(2000, 2, 30)
    # Negative day
    with pytest.raises(ValueError):
        generate_date_of_birth_sequence(2000, 1, -1)