from src.classes import Product


class Smartphone(Product):
    """Дочерний класс от класса Продукт"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float | None,
        model: str | None,
        memory: int | None,
        color: str | None,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            total_price = self.quantity * self.price + other.quantity * other.price
            return Smartphone(f"{self.name}+{other.name}", "Сумма", total_price, 1, None, None, None, None)
        raise TypeError("Можно складывать данные только одного класса")


class LawnGrass(Product):
    """Дочерний класс от класса Продукт"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str | None,
        germination_period: str | None,
        color: str | None,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            total_price = self.quantity * self.price + other.quantity * other.price
            return LawnGrass(f"{self.name}+{other.name}", "Сумма", total_price, 1, None, None, None)
        raise TypeError("Можно складывать данные только одного класса")
