"""Module for testing the main module."""

import pytest

from src.main import add_two_numbers, subtract_two_numbers


@pytest.mark.parametrize(
    "num1, num2, expected_result",
    [
        (3, 5, 8),  # Test adding two positive numbers
        (-9, 7, -2),  # Test adding one positive and one negative number
        (0, 9, 9),  # Test adding zero
        (10, -4, 6),  # Test adding one negative number to a positive
        (-8, -3, -11),  # Test adding two negative numbers
    ],
)
def test_add_two_numbers(num1, num2, expected_result):
    """Test adding two numbers."""
    result = add_two_numbers(num1, num2)
    assert result == expected_result
    assert isinstance(result, int)


@pytest.mark.parametrize(
    "num1, num2, expected_result",
    [
        (8, 3, 5),  # Test subtracting two positive numbers
        (-2, 7, -9),  # Test subtracting from a negative number a positive number
        (0, 9, -9),  # Test from zero to a positive number
        (10, -4, 14),  # Test subtracting one negative number from a positive
        (-8, -3, -5),  # Test subtracting two negative numbers
    ],
)
def test_subtract_two_numbers(num1, num2, expected_result):
    """Test subtracting two numbers."""
    result = subtract_two_numbers(num1, num2)
    assert result == expected_result
    assert isinstance(result, int)
