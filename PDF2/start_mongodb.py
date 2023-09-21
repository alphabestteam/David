import pymongo  # type: ignore


def insert_family(family_col, family):
    family_col.insert_many(family)


def insert_friends(friends_col, friends):
    for friend in friends:
        friends_col.insert_one(friend)


def insert_army(army_col, army):
    army_col.insert_many(army)


def print_cols(*cols):
    for col in cols:
        print("_" * 20)
        for doc in col:
            print(doc)


def get_cursors(family_col, friends_col, army_col):
    family_cursor = family_col.find({})
    friends_cursor = friends_col.find({})
    army_cursor = army_col.find({})

    return family_cursor, friends_cursor, army_cursor


def main():
    connection_str = "mongodb://localhost:27017"
    client = pymongo.MongoClient(connection_str)

    # db
    mydb = client["Aviv's_people"]

    # cols
    family_col = mydb["family"]
    friends_col = mydb["friends"]
    army_col = mydb["army"]

    family = [{"name": "mother", "age": 45, "occupation": "teacher"},
              {"name": "father", "age": 46, "occupation": "engineer"},
              {"name": "brother", "age": 12, "occupation": "school"},
              {"name": "sister", "age": 24, "occupation": "student"}]

    friends = [{"name": "Amit", "age": 20, "occupation": "waiter"},
               {"name": "Yonatan", "age": 24, "occupation": "doctor"},
               {"name": "Noa", "age": 22, "occupation": "student"},
               {"name": "Michal", "age": 21, "occupation": "baker"}]

    army = [{"_id": 1, "name": "Aviv", "age": 20, "occupation": "backend"},
            {"_id": 2, "name": "Lihi", "age": 21, "occupation": "QA"},
            {"_id": 3, "name": "Gabi", "age": 22, "occupation": "DevOps"},
            {"_id": 4, "name": "Ori", "age": 23, "occupation": "Front-end"},
            {"_id": 5, "name": "Ido", "age": 22, "occupation": "developer"},
            {"_id": 6, "name": "Yarden", "age": 24, "occupation": "DevOps"}]

    insert_family(family_col, family)  # Uses insert_many()
    insert_friends(friends_col, friends)  # Uses insert_one()
    insert_army(army_col, army)

    # get cursors for each col

    family_cursor, friends_cursor, army_cursor = get_cursors(
        family_col, friends_col, army_col)
    print("Before Delete:")
    print_cols(family_cursor, friends_cursor, army_cursor)

    lihi = {"name": "Lihi"}
    army_col.delete_one(lihi)

    family_cursor, friends_cursor, army_cursor = get_cursors(
        family_col, friends_col, army_col)
    print("After Delete: ")
    print_cols(family_cursor, friends_cursor, army_cursor)


if __name__ == '__main__':
    main()
