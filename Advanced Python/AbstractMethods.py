# ============================================================================
# SECTION 5: ABSTRACT METHODS (@abstractmethod)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 5: ABSTRACT METHODS")
print("=" * 60)

"""
What is @abstractmethod?
------------------------
An abstract method is a method declared in a base class that must be
implemented by any concrete (non-abstract) subclass. It's like a contract.

Use @abstractmethod when:
- You want to define an interface that subclasses must follow
- You want to prevent instantiation of the base class
- You want to ensure certain methods are implemented in subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    This class cannot be instantiated directly. Any subclass must
    implement all abstract methods.
    """

    def __init__(self, name):
        """
        Initialize an animal with a name.

        Args:
            name (str): The animal's name
        """
        self.name = name

    @abstractmethod
    def make_sound(self):
        """
        Abstract method for making a sound.

        Every animal subclass must implement this method.
        This ensures all animals can make a sound, but each
        animal makes their own unique sound.
        """
        pass

    @abstractmethod
    def move(self):
        """
        Abstract method for movement.

        Every animal subclass must implement this method.
        """
        pass

    def sleep(self):
        """
        Concrete method (not abstract).

        This method has an implementation and doesn't need to be
        overridden by subclasses (but it can be).
        """
        print(f"  {self.name} is sleeping... 😴")


class Dog(Animal):
    """Concrete implementation of Animal for dogs."""

    def make_sound(self):
        """Dogs bark."""
        print(f"  {self.name} says: Woof! Woof! 🐕")

    def move(self):
        """Dogs run."""
        print(f"  {self.name} is running on four legs! 🏃")


class Bird(Animal):
    """Concrete implementation of Animal for birds."""

    def make_sound(self):
        """Birds chirp."""
        print(f"  {self.name} says: Tweet! Tweet! 🐦")

    def move(self):
        """Birds fly."""
        print(f"  {self.name} is flying in the sky! 🦅")


# Using abstract methods
print("\nExample 9: Abstract Methods")
dog = Dog("Buddy")
dog.make_sound()
dog.move()
dog.sleep()

print()
bird = Bird("Tweety")
bird.make_sound()
bird.move()
bird.sleep()

print("\nExample 10: Cannot instantiate abstract class")
try:
    # This will raise an error because Animal is abstract
    animal = Animal("Generic")
except TypeError as e:
    print(f"  ❌ Error: {e}")


