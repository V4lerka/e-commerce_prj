class Product:
    """Класс "Продукт", включает атрибуты: название, описание, цена и кол-во на складе"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_params: dict, list_products: list[Product]) -> Product | None:
        """Класс-метод: принимает параметры товара в виде словаря, список имеющихся товаров класса "Продукт"
        и возвращает объект класса Product, если его нет в списке. Если продукт существует, тогда обновляет количество
        товара и обновляет цену товара, если она выше уже существующей"""

        for product in list_products:
            if product_params.get("name") == product.name:
                product.quantity += product_params.get("quantity", 0)
                new_price = product_params.get("price", 0)
                if new_price > product.price:
                    product.price = new_price
                return None
        return cls(**product_params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_value: float | int):
        if new_value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_value < self.__price:
            user_agree = input("Подтверждаете снижение цены? (y/n):\n")
            if user_agree.lower().strip() == "y":
                self.__price = new_value
            else:
                return
        self.__price = new_value


class Category:
    """Класс "Категория товара", включает атрибуты: название, описание, список продуктов в категории, количество
    продуктов и количество самих категорий"""

    name: str
    description: str
    products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод добавляет объект класса Product к списку товаров приватного атрибута __products"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Метод-геттер: выводит список товаров категории в виде строки"""
        list_products = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        ]
        return "\n".join(list_products)
