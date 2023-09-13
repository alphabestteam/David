from customer import Customer
from register import Register
import json


def get_cart_items(purchase: dict) -> list:
    return [[item["product"].name, item["product"].price, item["quantity"]] for item in purchase["shopping_list"]]


def handle_json(registers: list[Register]) -> None:
    summery = {"summery": []}
    for register in registers:
        for purchase in register.total_sales_history:
            print(purchase["shopping_list"])
            summery["summery"].append(
                {"customer": purchase['user_name'], "cart": get_cart_items(purchase), "total": purchase['total']})
    print(summery)
    with open("profits.JSON", 'w') as json_file:
        json.dump(summery, json_file)


def main() -> None:
    registers = []

    register1 = Register()
    register2 = Register()
    registers.append(register1)
    registers.append(register2)

    customer1 = Customer("David")
    customer2 = Customer("Chaim")

    customer1.add_product("apple", 20, 10)
    customer1.add_product("orange", 10, 3)

    customer1.remove_product("apple", 3)
    customer1.remove_product("orange", 3)
    customer1.remove_product("apple", 300)
    customer1.remove_product("water", 3)

    customer2.add_product("apple", 20, 10)
    customer2.add_product("orange", 10, 3)
    customer2.add_product("banana", 10, 3)

    customer2.remove_product("apple", 3)
    customer2.remove_product("orange", 3)
    customer2.remove_product("apple", 300)
    customer2.remove_product("water", 3)

    register1.checkout_customer(customer1)
    register1.checkout_customer(customer2)
    register1.print_summary()

    handle_json(registers)


if __name__ == '__main__':
    main()


