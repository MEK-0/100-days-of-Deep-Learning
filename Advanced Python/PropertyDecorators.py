# ============================================================================
# SECTION 2: PROPERTY DECORATORS (@property, @setter, @deleter)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 2: PROPERTY DECORATORS")
print("=" * 60)

"""
What are Property Decorators?
------------------------------
Property decorators allow you to define methods that can be accessed like 
attributes. This is useful for:
- Data validation
- Computed attributes
- Controlling access to private data
"""


class Person:
    """
    A class demonstrating property decorators.
    
    Properties allow us to add validation and logic when getting/setting
    attributes, while still using simple attribute syntax.
    """
    
    def __init__(self, name, age):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.__name = name  # Private attribute (convention: starts with __)
        self.__age = age
    
    @property
    def name(self):
        """
        Getter for name property.
        
        The @property decorator allows us to access _name like a regular
        attribute (person.name) instead of calling a method (person.name()).
        
        Returns:
            str: The person's name
        """
        print("  📖 Getting name...")
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Setter for name property with validation.
        
        This is called when you try to assign a value: person.name = "John"
        We can add validation logic here.
        
        Args:
            value (str): The new name value
            
        Raises:
            ValueError: If name is empty or not a string
        """
        print(f"  ✏️  Setting name to: {value}")
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty!")
        self.__name = value
    
    @name.deleter
    def name(self):
        """
        Deleter for name property.
        
        This is called when you use: del person.name
        Useful for cleanup operations.
        """
        print("  🗑️  Deleting name...")
        self.__name = None
    
    @property
    def age(self):
        """
        Getter for age property.
        
        Returns:
            int: The person's age
        """
        return self.__age
    
    @age.setter
    def age(self, value):
        """
        Setter for age property with validation.
        
        Args:
            value (int): The new age value
            
        Raises:
            ValueError: If age is negative or not an integer
        """
        if not isinstance(value, int):
            raise ValueError("Age must be an integer!")
        if value < 0:
            raise ValueError("Age cannot be negative!")
        if value > 150:
            raise ValueError("Age seems unrealistic!")
        self.__age = value
    
    @property
    def is_adult(self):
        """
        A computed property (read-only).
        
        This property doesn't have a setter - it's calculated from age.
        This demonstrates how properties can compute values on-the-fly.
        
        Returns:
            bool: True if person is 18 or older
        """
        return self.__age >= 18


# Using property decorators
print("\nExample 3: Using @property")
person = Person("Bob", 25)
print(f"Name: {person.name}")  # Calls the getter
print(f"Age: {person.age}")
print(f"Is adult? {person.is_adult}")

print("\nExample 4: Using @setter")
person.name = "Robert"  # Calls the setter
person.age = 26

print("\nExample 5: Property validation")
try:
    person.age = -5  # This will raise an error
except ValueError as e:
    print(f"  ❌ Error: {e}")

print("\nExample 6: Using @deleter")
del person.name  # Calls the deleter
print(f"Name after deletion: {person.name}")
