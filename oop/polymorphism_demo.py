import math

class Shape:
    """Base class representing a geometric shape"""
    def area(self):
        """Calculate area of the shape (to be overridden by subclasses)"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Derived class representing a rectangle"""
    def __init__(self, length, width):
        """
        Initialize rectangle with length and width
        Args:
            length (float): Length of rectangle
            width (float): Width of rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area of rectangle (overrides Shape.area())"""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle"""
    def __init__(self, radius):
        """
        Initialize circle with radius
        Args:
            radius (float): Radius of circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate area of circle (overrides Shape.area())"""
        return math.pi * (self.radius ** 2)