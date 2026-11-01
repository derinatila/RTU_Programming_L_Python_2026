"""
Task 1 – Simple Function with Arithmetic
----------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.

    area = π × radius²

Requirements:
- Use `math.pi` from the math module (not 3.14).
- The function RETURNS the full, unrounded float. Rounding to 2 decimals
  happens only when printing in the main block.
- You may assume radius >= 0.

In the main block: ask the user for a radius, convert it to a float,
call circle_area(), and print the result with 2 decimals.
"""

import math


def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius (unrounded)."""
    return math.pi * (radius**2)


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    radius_str = input("Enter radius: ")
    radius = float(radius_str)
    area = circle_area(radius)

    # Round to 2 decimals only when printing
    print(f"Area of the circle: {area:.2f}")
