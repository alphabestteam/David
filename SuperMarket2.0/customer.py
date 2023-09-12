from typing import List, Any

from product import Product


def get_price_per_unit(price: float, quantity: int) -> float:
    return quantity / price


class Customer:
    def __init__(self, name: str) -> None:
        self._name = name
        self._shopping_list = []  # [ product1 ]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def shopping_list(self) -> list[dict[object, int]]:
        return self._shopping_list

    def __str__(self):
        product_info = []
        for product in self.shopping_list:
            product_info.append(f"product name: {product['product'].name}, product price: {product['product'].price}, Quantity: {product['quantity']}")
        return "\n".join(product_info)

    @shopping_list.setter
    def shopping_list(self, item: dict) -> None:
        self._shopping_list = item

    def add_product(self, item_name: str, item_price: float, item_quantity: int) -> None:
        for product in self.shopping_list:
            if product["product"].name == item_name:
                print("That item is already in your shopping list")
                print(f"Adding {item_quantity} more {item_name} to your list")
                product["quantity"] += item_quantity
                return

        self.shopping_list.append({"product": Product(item_name, item_price), "quantity": item_quantity})
        print(f"Successfully added {item_name} to your shopping list")

    def remove_product(self, item_name: str, remove_amount: int) -> None:
        for product in self.shopping_list:
            if product["product"].name == item_name:
                if product["quantity"] < remove_amount:
                    print(f"You cant remove {remove_amount} since you only have {product['quantity']} left.")
                    return

                if product["quantity"] > remove_amount:
                    product["quantity"] -= remove_amount
                    print(f"Successfully removed {remove_amount} from {item_name}")
                    return

                del product
                print(f"Successfully removed {item_name} from your shopping list")
                return
        print(f"The item {item_name} is not in your list")
