# ============================================================================
# SECTION 6: FUNCTION OVERLOADING (@overload)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 6: FUNCTION OVERLOADING")
print("=" * 60)

"""
What is @overload?
------------------
Python doesn't have traditional function overloading like Java or C++.
The @overload decorator is used for type hints to indicate that a function
can accept different combinations of argument types.

Note: @overload only provides type hints for static type checkers (like mypy).
You still need to write one actual implementation.
"""

from typing import overload, Union


class Calculator:
    """A calculator demonstrating function overloading with type hints."""

    @overload
    def add(self, a: int, b: int) -> int:
        ...

    @overload
    def add(self, a: int, b: int, c: int) -> int:
        ...

    def add(self, a: int, b: int, c: int | None = None) -> int:
        if c is None:
            return a + b
        return a + b + c

    @overload
    def process(self, value: int) -> int:
        """Process an integer."""
        ...

    @overload
    def process(self, value: str) -> str:
        """Process a string."""
        ...

    def process(self, value: Union[int, str]) -> Union[int, str]:
        """
        Process a value (actual implementation).

        The @overload decorators above are just type hints.
        This is the actual implementation that handles both cases.

        Args:
            value: Either an int or a str

        Returns:
            If int: returns value * 2
            If str: returns value in uppercase
        """
        if isinstance(value, int):
            print(f"  Processing integer: {value}")
            return value * 2
        elif isinstance(value, str):
            print(f"  Processing string: {value}")
            return value.upper()
        else:
            raise TypeError("Value must be int or str")


# Using overloaded functions
print("\nExample 11: Function Overloading")
calc = Calculator()
result1 = calc.process(5)
print(f"  Result: {result1}")

result2 = calc.process("hello")
print(f"  Result: {result2}")
