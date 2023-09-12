import json


def get_json_data(file_name: str) -> any:
    with open(file_name, 'r') as config_file:
        data = json.load(config_file)
        return data


def create_and_init_json_file(file_name: str, name: str, city: str, age: int) -> None:
    user_info = {"name": name, "city": city, "age": age}
    with open(file_name, 'w') as json_file:
        json.dump(user_info, json_file)


if __name__ == '__main__':
    json_data = get_json_data("personInfo.JSON")
    print(json_data)
    create_and_init_json_file("MyAddress.JSON", "David", "Beit Shemesh", 21)

