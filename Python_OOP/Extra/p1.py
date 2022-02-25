#!/usr/bin/env python3

import math

class Point:
    """
    The following initialization function to the Point Class
    requires the user, upon the Point Object's instantiation,
    to assign values to x & y
    """
    def __init__(self, x: float, y: float) ->None:
        self.x = x
        self.y = y

    # The first method needs accept arguments
    # x & y that set a value on the self
    def move(self, x: float, y: float) -> None:
        self.x = 0
        self.y = 0

    def reset(self) -> None:
        """Call the move method above"""
        self.move(0, 0)

    # Lastly, calculate the Euclidian distance
    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


# Create a point instance:
point = Point(3, 5)
print(point.x, point.y)
