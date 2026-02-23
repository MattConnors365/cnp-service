from cnp_toolkit.checksum import generate_checksum
import pytest


def test_valid_checksum():
    assert generate_checksum("196052342114") == 1


def test_invalid_length():
    with pytest.raises(ValueError):
        generate_checksum("123")


def test_non_digit_input():
    with pytest.raises(ValueError):
        generate_checksum("12345678901A")