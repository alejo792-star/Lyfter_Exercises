class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return"It makes a sound."

class Dog(Animal):
    def speak(self):
        return "guaw 🐶"

class Cat(Animal):
    def speak(self):
        return "miau 🐱"

def main():
    dog = Dog("Firulais")
    cat = Cat("michi")
    other_animal = Animal("pepito")
    print(dog.speak())
    print(cat.speak())
    print(other_animal.speak())


if __name__ == "__main__":
    main()