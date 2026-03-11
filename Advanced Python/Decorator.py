"""
PYTHON ADVANCED FEATURES TUTORIAL
==================================

Dekoratörler, mevcut bir fonksiyonun koduna dokunmadan ona yeni özellikler eklemeni sağlayan yapılardır. Python'da fonksiyonlar "birinci sınıf nesne" (first-class citizens) olduğu için başka bir fonksiyona parametre olarak gönderilebilirler.

Mantık: Bir fonksiyonu "paketler" (wrap), öncesinde veya sonrasında işlem yapar.

Kullanım: Loglama, yetki kontrolü veya çalışma süresi ölçümü gibi durumlarda kullanılır.
"""

print("=" *60)
print("Section 1: BASIC DECORATORS")
print("="*60)


def my_decarator(func):
    """
        A simple decorator that adds behavior before and after a function call.

        Args:
            func: The function to be decorated

        Returns:
            wrapper: A new function that wraps the original function
        """
    def wrapper():
        print("🎁 Something is happening before the function is called.")
        func()
        print("🎁 Something is happening before the function is called.")
    return wrapper

@my_decarator
def say_hello():
    """A simple function that will be decorated"""
    print("Hello")

#Using the decarator
print("\nExample 1: Basic Decarator ")
say_hello()

def repeat_three_times(func):
    """
        A decorator that repeats a function call three times.

        Args:
            func: The function to be repeated

        Returns:
            wrapper: A function that calls the original three times
    """
    def wrapper(*args, **kwargs):
        for i in range(3):
            print(f" Call #{i+1}:")
            func(*args,**kwargs)
    return wrapper


@repeat_three_times
def greet(name):
    """Greet someone by name."""
    print(f" Hello, {name}!")

print("\nExample 2: Decarator with Arguments")
greet("Alice")

print("="*60)
print("FINISH")
print("="*60)