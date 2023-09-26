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

    # These are here to stop the programming from throwing errors if you rerun the program. (since the collections already exist we drop them and rebuild)
    # mydb["family"].drop()
    # mydb["friends"].drop()
    # mydb["army"].drop()

    # cols
    family_col = mydb["family"]
    friends_col = mydb["friends"]
    army_col = mydb["army"]

    family = [{"name": "mother", "age": 45, "role": "teacher"},
              {"name": "father", "age": 46, "role": "engineer"},
              {"name": "brother", "age": 12, "role": "school"},
              {"name": "sister", "age": 24, "role": "student"}]

    friends = [{"name": "Amit", "age": 20, "role": "waiter"},
               {"name": "Yonatan", "age": 24, "role": "doctor"},
               {"name": "Noa", "age": 22, "role": "student"},
               {"name": "Michal", "age": 21, "role": "baker"}]

    army = [{"_id": 1, "name": "Aviv", "age": 20, "role": "backend"},
            {"_id": 2, "name": "Lihi", "age": 21, "role": "QA"},
            {"_id": 3, "name": "Gabi", "age": 22, "role": "DevOps"},
            {"_id": 4, "name": "Ori", "age": 23, "role": "Front-end"},
            {"_id": 5, "name": "Ido", "age": 22, "role": "developer"},
            {"_id": 6, "name": "Yarden", "age": 24, "role": "DevOps"}]

    insert_family(family_col, family)  # Uses insert_many()
    insert_friends(friends_col, friends)  # Uses insert_one()
    insert_army(army_col, army)

    # get cursors for each col

    family_cursor, friends_cursor, army_cursor = get_cursors(
        family_col, friends_col, army_col)
    print_cols(family_cursor, friends_cursor, army_cursor)

    lihi = {"name": "Lihi"}
    army_col.delete_one(lihi)

    # PDF 3 starts from here
    candidate = army_col.find_one({"role": "DevOps", "age": {'$lt': 23}})
    print("Good Candidate: ", candidate)

    avivs_other_friend = army_col.find_one(
        {"age": candidate["age"], "_id": {'$ne': candidate["_id"]}})  # Get friend other friend
    # set Gabi's old role to other friends role
    army_col.update_one(
        candidate, {'$set': {"role": avivs_other_friend["role"]}})

    # Sort the collection
    army_col.aggregate([
        {'$sort': {'age': -1}}, {"$out": "army"}
    ])
    army_cursor = army_col.find({})

    print("Sorted collection printed:")
    for army_friend in army_cursor:
        print(army_friend)
        if army_friend['age'] > 23:
            friends_col.insert_one(army_friend)
            army_col.delete_one(army_friend)


if __name__ == '__main__':
    main()
