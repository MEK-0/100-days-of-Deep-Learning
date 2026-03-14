# ============================================================================
# SECTION 8: OVERRIDE DECORATOR (@override)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 8: OVERRIDE DECORATOR")
print("=" * 60)

"""
What is @override?
------------------
The @override decorator (available in Python 3.12+) explicitly marks
that a method is intended to override a parent class method. This helps
catch errors where you think you're overriding a method but actually aren't
(due to typos or signature mismatches).

Note: If your Python version is < 3.12, you can use typing_extensions.
"""

try:
    from typing import override
except ImportError:
    # For Python < 3.12, use typing_extensions
    from typing_extensions import override


class Shape:
    """Base class for shapes."""
    
    def area(self) -> float:
        """
        Calculate area of the shape.
        
        Returns:
            float: The area
        """
        return 0.0
    
    def perimeter(self) -> float:
        """
        Calculate perimeter of the shape.
        
        Returns:
            float: The perimeter
        """
        return 0.0


class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, width: float, height: float):
        """
        Initialize a rectangle.
        
        Args:
            width (float): Width of the rectangle
            height (float): Height of the rectangle
        """
        self.width = width
        self.height = height
    
    @override
    def area(self) -> float:
        """
        Calculate rectangle area.
        
        The @override decorator tells type checkers: "I'm intentionally
        overriding the parent's area method." If there was no area method
        in the parent, the type checker would warn you.
        
        Returns:
            float: Width times height
        """
        return self.width * self.height
    
    @override
    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter.
        
        Returns:
            float: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, radius: float):
        """
        Initialize a circle.
        
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    @override
    def area(self) -> float:
        """
        Calculate circle area.
        
        Returns:
            float: π * radius²
        """
        import math
        return math.pi * self.radius ** 2
    
    @override
    def perimeter(self) -> float:
        """
        Calculate circle circumference.
        
        Returns:
            float: 2 * π * radius
        """
        import math
        return 2 * math.pi * self.radius


# Using override decorator
print("\nExample 14: Override Decorator")
rect = Rectangle(5, 3)
print(f"Rectangle (5x3):")
print(f"  Area: {rect.area():.2f}")
print(f"  Perimeter: {rect.perimeter():.2f}")

print()
circle = Circle(4)
print(f"Circle (radius=4):")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")

