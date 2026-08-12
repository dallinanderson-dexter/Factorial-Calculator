"""Command-line factorial calculator."""

from __future__ import annotations

import argparse


def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("number must be non-negative")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate a factorial.")
    parser.add_argument("number", type=int, help="a non-negative integer")
    args = parser.parse_args()

    try:
        print(factorial(args.number))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
