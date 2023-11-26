"""Main module of the project."""

from datetime import datetime


def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract_two_numbers(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


if __name__ == "__main__":
    today = datetime.today()  # pragma: no cover
    print(f"Today is {today}")  # pragma: no cover
    print(add_two_numbers(1, 2))  # pragma: no cover
    print(subtract_two_numbers(1, 2))  # pragma: no cover
