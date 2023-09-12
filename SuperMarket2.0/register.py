def sum_shopping_list(shopping_list) -> float:
    product_sum = 0
    for item in shopping_list:
        product_sum += item["product"].price*item["quantity"]
    return product_sum


class Register:
    def __init__(self):
        self._total_cash = 0
        self._total_sales_history = []  # will contain name and amount for each person who bought something

    def checkout_customer(self, customer: object) -> None:
        user_name_and_payment = {"user_name": customer.name, "shopping_list": customer.shopping_list}
        self.total_sales_history = user_name_and_payment
        self.total_cash = sum_shopping_list(customer.shopping_list)

    def print_summary(self):
        print("_"*20)
        print(f"This registers gross-income: {self.total_cash}")
        print("List of purchases")
        for purchase in self._total_sales_history:
            print(f"\nUser: {purchase['user_name']},\nlist of products info:")
            for product in purchase['shopping_list']:
              print(f"Product Name: {product['product'].name}, Product Price: {product['product'].price}, Quantity: {product['quantity']}")
        print("_"*20)

    @property
    def total_cash(self) -> float or int:
        return self._total_cash

    @total_cash.setter
    def total_cash(self, new_total_cash: float or int) -> None:
        self._total_cash = new_total_cash

    @property
    def total_sales_history(self) -> list:
        return self._total_sales_history

    @total_sales_history.setter
    def total_sales_history(self, name_and_sold_for: dict) -> None:
        self._total_sales_history.append(name_and_sold_for)
