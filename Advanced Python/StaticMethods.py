"""
============================================================
Section 3: Static Methods
============================================================
"""
print("\n" + "="*60)
print("Section 3: Static Methods")
print("="*60)

class MathOperations:
    """A class containing math utility functions."""
    @staticmethod
    def add(x,y,):
        return x+y

    @staticmethod
    def multiply(x,y):
        return x * y

    @staticmethod
    def is_even(number):
        """Check if a number is even

        Args:
            number (int): Number to check

        Returns:
            bool: True if even , false if odd
        """
        return number % 2 == 0


#Using static methods
print("\nExamples 7: Static Methods:")
print(f"5+3 = {MathOperations.add(5,3)}")
print(f"5*3 = {MathOperations.multiply(5,3)}")
print(f"IS even 4 ? {MathOperations.is_even(4)}")
print(f"Is even 7 ? {MathOperations.is_even(7)}")

# You can also call static methods on instances (but it's not common)

math_ops = MathOperations()
print(f"instance call: 10 + 5 = {math_ops.add(10,5)}")