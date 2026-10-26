"""Exercise 03: one clear basic inheritance example."""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


dog = Dog("Buddy")
print(f"{dog.name}: {dog.speak()}")

# Dog is an Animal because Dog inherits Animal's name attribute and can be used
# wherever a general Animal object is expected.
