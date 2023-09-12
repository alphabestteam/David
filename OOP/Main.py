from Person import Person


def initialize_people_into_list(people_list: list) -> None:
    for _ in range(10):
        people_list.append(Person())


def print_people_in_list(people_list: list) -> None:
    for person in people_list:
        print(person)


if __name__ == "__main__":
    people_list = []
    initialize_people_into_list(people_list)
    print_people_in_list(people_list)
