"""Main module of the project."""

from datetime import datetime


def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# def subtract_two_numbers(a: int, b: int) -> int:
#     """Subtract two numbers."""
#     return a - b


if __name__ == "__main__":
    today = datetime.today()
    print(f"Today is {today}")
    print(add_two_numbers(1, 2))
    print(subtract_two_numbers(1, 2))
