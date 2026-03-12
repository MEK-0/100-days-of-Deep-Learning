# ============================================================================
# SECTION 4: CLASS METHODS (@classmethod)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 4: CLASS METHODS")
print("=" * 60)

"""
What is @classmethod?
---------------------
A class method receives the class itself as the first argument (cls)
instead of an instance (self). It can access and modify class-level data.

Use @classmethod for:
- Alternative constructors (factory methods)
- Methods that need to access or modify class variables
"""


class Pizza:
    """A class demonstrating class methods for alternative constructors."""

    # Class variable (shared by all instances)
    total_pizzas_made = 0

    def __init__(self, ingredients):
        """
        Initialize a Pizza with given ingredients.

        Args:
            ingredients (list): List of ingredient strings
        """
        self.ingredients = ingredients
        Pizza.total_pizzas_made += 1

    def __repr__(self):
        """String representation of the pizza."""
        return f"Pizza({', '.join(self.ingredients)})"

    @classmethod
    def margherita(cls):
        """
        Factory method to create a Margherita pizza.

        This is a class method that acts as an alternative constructor.
        Instead of Pizza(['tomato', 'mozzarella', 'basil']), you can
        simply call Pizza.margherita().

        Returns:
            Pizza: A Margherita pizza instance
        """
        return cls(['tomato sauce', 'mozzarella', 'basil'])

    @classmethod
    def pepperoni(cls):
        """
        Factory method to create a Pepperoni pizza.

        Returns:
            Pizza: A Pepperoni pizza instance
        """
        return cls(['tomato sauce', 'mozzarella', 'pepperoni'])

    @classmethod
    def get_total_pizzas(cls):
        """
        Get the total number of pizzas created.

        This class method accesses the class variable total_pizzas_made.

        Returns:
            int: Total number of pizzas created
        """
        return cls.total_pizzas_made


# Using class methods
print("\nExample 8: Class Methods as Factory Methods")
pizza1 = Pizza.margherita()
pizza2 = Pizza.pepperoni()
pizza3 = Pizza(['BBQ sauce', 'chicken', 'onions'])

print(f"Pizza 1: {pizza1}")
print(f"Pizza 2: {pizza2}")
print(f"Pizza 3: {pizza3}")
print(f"Total pizzas made: {Pizza.get_total_pizzas()}")


