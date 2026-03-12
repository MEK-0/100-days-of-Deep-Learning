# ============================================================================
# SECTION 7: FINAL CLASSES AND METHODS (@final)
# ============================================================================

print("\n" + "=" * 60)
print("SECTION 7: FINAL DECORATOR")
print("=" * 60)

"""
What is @final?
---------------
The @final decorator indicates that a class should not be subclassed,
or a method should not be overridden. This is a type checking hint
for static type checkers like mypy.

Note: Python won't prevent you from subclassing or overriding at runtime,
but type checkers will warn you.
"""

from typing import final


class BaseGame:
    """A base game class with final and non-final methods."""

    def start(self):
        """Start the game - can be overridden by subclasses."""
        print("  🎮 Game starting...")

    @final
    def calculate_score(self, points: int) -> int:
        """
        Calculate score - marked as final.

        This method should NOT be overridden by subclasses because
        the scoring logic must remain consistent.

        Args:
            points (int): Base points earned

        Returns:
            int: Final score with bonus
        """
        bonus = 100
        return points + bonus

    def end(self):
        """End the game - can be overridden by subclasses."""
        print("  🏁 Game over!")


class MyGame(BaseGame):
    """A specific game implementation."""

    def start(self):
        """Override start method (this is allowed)."""
        print("  🎮 MyGame starting with custom intro!")

    # If you uncomment this, a type checker would warn you:
    # def calculate_score(self, points: int) -> int:
    #     # ❌ Type checker warning: Cannot override final method
    #     return points * 2


@final
class SecretAlgorithm:
    """
    A class marked as final - should not be subclassed.

    Use @final on classes when you don't want them to be extended,
    perhaps for security or consistency reasons.
    """

    def process(self):
        """Process data with secret algorithm."""
        print("  🔒 Processing with secret algorithm...")


# Using final decorator
print("\nExample 12: Final Methods")
game = MyGame()
game.start()
score = game.calculate_score(50)
print(f"  Final score: {score}")
game.end()

print("\nExample 13: Final Class")
secret = SecretAlgorithm()
secret.process()

# If you uncomment this, a type checker would warn you:
# class MySecretAlgorithm(SecretAlgorithm):  # ❌ Type checker warning
#     pass


