"""Module for testing the main module."""

from src.main import add_two_numbers


def test_add_two_numbers_positive() -> None:
    """Test two positive numbers."""
    result = add_two_numbers(3, 5)
    assert result == 8


def test_add_two_numbers_negative() -> None:
    """Test one positive and one negative number."""
    result = add_two_numbers(-2, 7)
    assert result == 5


def test_add_two_numbers_zero() -> None:
    """Test adding zero."""
    result = add_two_numbers(0, 9)
    assert result == 9


def test_add_two_numbers_negative_result() -> None:
    """Test adding one negative number to a positive."""
    result = add_two_numbers(10, -4)
    assert result == 6


def test_add_two_numbers_both_negative() -> None:
    """Test adding two negative numbers."""
    result = add_two_numbers(-8, -3)
    assert result == -11


def test_add_two_numbers_type() -> None:
    """Test add_two_numbers results type."""
    result = add_two_numbers(3, 5)
    assert isinstance(result, int)

    result = add_two_numbers(-2, 7)
    assert isinstance(result, int)

    result = add_two_numbers(0, 9)
    assert isinstance(result, int)

    result = add_two_numbers(10, -4)
    assert isinstance(result, int)

    result = add_two_numbers(-8, -3)
    assert isinstance(result, int)


# def test_subtract_two_numbers_positive() -> None:
#     """Test subtracting two positive numbers."""
#     result = subtract_two_numbers(8, 3)
#     assert result == 5


# def test_subtract_two_numbers_negative() -> None:
#     """Test subtracting from a negative number a positive number."""
#     result = subtract_two_numbers(-2, 7)
#     assert result == -9


# def test_subtract_two_numbers_zero() -> None:
#     """Test from zero to a positive number."""
#     result = subtract_two_numbers(0, 9)
#     assert result == -9


# def test_subtract_two_numbers_negative_result() -> None:
#     """Test subtracting one negative number from a positive."""
#     result = subtract_two_numbers(10, -4)
#     assert result == 14


# def test_subtract_two_numbers_both_negative() -> None:
#     """Test subtracting two negative numbers."""
#     result = subtract_two_numbers(-8, -3)
#     assert result == -5


# def test_subtract_two_numbers_type() -> None:
#     """Test subtract_two_numbers results type."""
#     result = subtract_two_numbers(8, 3)
#     assert isinstance(result, int)

#     result = subtract_two_numbers(-2, 7)
#     assert isinstance(result, int)

#     result = subtract_two_numbers(0, 9)
#     assert isinstance(result, int)

#     result = subtract_two_numbers(10, -4)
#     assert isinstance(result, int)

#     result = subtract_two_numbers(-8, -3)
#     assert isinstance(result, int)
