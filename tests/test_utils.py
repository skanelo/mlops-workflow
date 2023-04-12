"""A module which is dedicated for testing the src/utils.py module."""

from src import utils


def test_add_two_random_numbers() -> None:
    """Test for the add_two_random_numbers function."""

    result = utils.add_two_random_numbers()
    assert isinstance(result, int)
