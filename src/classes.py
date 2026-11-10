


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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            total_price = self.quantity * self.__price + other.quantity * other.price
            return Product(f"{self.name}+{other.name}", "Сумма", total_price, 1)
        raise TypeError

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

    def __str__(self):
        total_amount = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_amount} шт."

    def add_product(self, product: Product) -> None:
        """Метод добавляет объект класса Product к списку товаров приватного атрибута __products"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавить только объект класса Продукт или дочернего класса")

    @property
    def products(self) -> str:
        """Метод-геттер: выводит список товаров категории в виде строки"""
        list_prods = [str(product) for product in self.__products]
        return "\n".join(list_prods)


class CategoryIterator:
    """Класс, с помощью которого можно будет перебирать все товары категории в цикле."""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        list_prods = self.category.products.split("\n")
        if self.index < len(list_prods):
            product = list_prods[self.index]
            self.index += 1
            return product
        raise StopIteration
