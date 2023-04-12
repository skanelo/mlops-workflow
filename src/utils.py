"""
This module contains a set of functions for performing basic math operations.

Functions:
    add(x, y): Adds two numbers together.

Dependencies:
    None

Example usage:
    >>> add(2, 3)
    5
"""
import random


def add_two_random_numbers() -> int:
    """
    Adds two random numbers.

    Returns:
        int: The sum of two numbers.
    """
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    return first_number + second_number
