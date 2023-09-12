from Exeptions_ListComprehensions.Person import Person


def get_people_over_18(person_list: list) -> list:
    return [person for person in person_list if person.age >= 18]


if __name__ == "__main__":
    person_list = [Person() for _ in range(10)]

    print("People that are 18 or older")
    [print(person) for person in get_people_over_18(person_list)]
