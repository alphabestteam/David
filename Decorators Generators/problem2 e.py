class People:
    def __init__(self):
        self._names_of_people = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.names_of_people) > 0:
            name = self.names_of_people[0]
            del self.names_of_people[0]
            return name
        else:
            raise StopIteration

    @property
    def names_of_people(self):
        return self._names_of_people

    @names_of_people.setter
    def names_of_people(self, value):
        self._names_of_people.append(value)

    def add_person(self, *names) -> None:
        for name in names:
            self.names_of_people = name


if __name__ == '__main__':
    people = People()
    people.add_person("David", "John", "Fred", "James")
    print(people.names_of_people)
    for p in people:
        print(p)
