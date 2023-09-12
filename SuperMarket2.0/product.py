class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"item name: {self.name}, item price: {self.price}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price
