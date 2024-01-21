# factory.py
class Animal:
    def speak(self):
        pass

    def perform_action(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def perform_action(self):
        return "Fetching the ball"


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def perform_action(self):
        return "Chasing a mouse"


class Duck(Animal):
    def speak(self):
        return "Quack!"

    def perform_action(self):
        return "Swimming in the pond"


class AnimalFactory:
    def create_animal(self, animal_type):
        animal_type_lower = animal_type.lower()
        if animal_type_lower == "dog":
            return Dog()
        elif animal_type_lower == "cat":
            return Cat()
        elif animal_type_lower == "duck":
            return Duck()
        else:
            raise ValueError("Invalid animal type")


# Example usage
animal_factory = AnimalFactory()
dog = animal_factory.create_animal("dog")
cat = animal_factory.create_animal("cat")
duck = animal_factory.create_animal("duck")

print(dog.speak())
print(dog.perform_action())

print(cat.speak())
print(cat.perform_action())

print(duck.speak())
print(duck.perform_action())
