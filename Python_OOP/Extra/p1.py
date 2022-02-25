#!/usr/bin/env python3

# use the mypy tool to check type hints
import math

class Point:
    """
    This class represents a point in two-dimensional geo corordinates.
    
    The following initialization function to the Point Class
    requires the user, upon the Point Object's instantiation,
    to assign values to x & y
    """
    def __init__(self, x: float, y: float) ->None:
        """
        Initialize the position of a new point. The x & y coordinates can be specified.
        However, if they are not, then the point defaults to the original.

        :param x: float x-cordinate
        :param y: float x-coordinate
        """
        self.move(x, y)

    # The first method needs accept arguments
    # x & y that set a value on the self
    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location in 2D space.

        :param x: float x-cordinate
        :param y: float x-coordinate
        """
        self.x = x
        self.y = y


    def reset(self) -> None:
        """
        Reset the point back to it's geometric origin by
        calling the move method above.
        """
        self.move(0, 0)

    # Lastly, calculate the Euclidian distance
    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate the Euclidian distance from this point
        to a second point passed as a parameter
        :param other: Point instance
        :return: float distance
        """
        return math.hypot(self.x - other.x, self.y - other.y)
        

test_main = """
>>> main()
p1.calculate_distance(p2)=5.0
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}


def main() -> None:
    """
    Does the useful work.
    >>> main()
    p1.calculate_distance(p2)=5.0
    """
    p1 = Point()
    p2 = Point(3, 4)
    print(f"{p1.calculate_distance(p2)=}")


if __name__ == "__main__":
    main()
