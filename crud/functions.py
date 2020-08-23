import math


def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [float, int]:
        raise TypeError("The radius must be a non-negative real number")

    return math.pi * r**2
