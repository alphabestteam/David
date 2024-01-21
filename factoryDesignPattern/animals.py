class Animal:
    def speak(self):
        pass

    def do_something(self):
        pass


class Dog(Animal):
    def speak(self):
        return "woff!"

    def do_something(self):
        return "Fetching a ball"


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def do_something(self):
        return "Chasing a mouse"


class AnimalFactory:
    def create_animal(self, animal):
        match animal.lower():
            case "dog":
                return Dog()
            case "cat":
                return Cat()
            case _:
                raise ValueError("Invalid animal type")


animal_factory = AnimalFactory()
dog = animal_factory.create_animal("dog")
cat = animal_factory.create_animal("cat")

print(dog.speak())
print(dog.do_something())

print("\n" + "-" * 20 + "\n")

print(cat.speak())
print(cat.do_something())
