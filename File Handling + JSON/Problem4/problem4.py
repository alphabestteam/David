import json


def get_json_info(file_name: str) -> any:
    with open(file_name, 'r') as config_file:
        info = json.load(config_file)
        return info


def change_to_upper(data: dict) -> None:
    data_upper_case = data["data"].upper()
    data["data"] = data_upper_case


def write_to_file(file_name: str, data: any) -> None:
    with open(file_name, 'w') as config_file:
        json.dump(data, config_file)


if __name__ == '__main__':
    data = get_json_info("config.JSON")
    change_to_upper(data)

    if data["silent"]:
        print(data["data"])

    write_to_file("config.JSON", data)
