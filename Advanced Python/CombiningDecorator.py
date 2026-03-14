# ============================================================================
#  SECTION: COMBINING DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("BONUS: COMBINING MULTIPLE DECORATORS")
print("=" * 60)

"""
You can stack multiple decorators on the same function or method.
They are applied from bottom to top (closest to the function first).
"""


def multiply_decorator(func):
    def wrapper(x: int):
        return func(x) * 2
    return wrapper


def other_decorator(func):
    def wrapper(x: int):
        return func(x) * 4
    return wrapper


@multiply_decorator
@other_decorator
def calculate(x: int):
    return x * 2


print(calculate(10))
