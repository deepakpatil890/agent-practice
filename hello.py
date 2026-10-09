"""A tiny practice script for the GitHub agent to read and explain."""

from datetime import date


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Today is {date.today():%A, %d %B %Y}."


def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


def is_even(number: int) -> bool:
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


if __name__ == "__main__":
    print(greet("Deepak"))
    print("2 + 3 =", add(2, 3))
    print("Is 7 even?", is_even(7))
