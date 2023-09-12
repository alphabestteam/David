from customer import Customer
from register import Register


def main():
    register1 = Register()
    register2 = Register()

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

    customer2.remove_product("apple", 3)
    customer2.remove_product("orange", 3)
    customer2.remove_product("apple", 300)
    customer2.remove_product("water", 3)

    register1.checkout_customer(customer1)
    register1.checkout_customer(customer2)
    register1.print_summary()


if __name__ == '__main__':
    main()


