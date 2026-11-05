class Product:
    """Класс "Продукт", включает атрибуты: название, описание, цена и кол-во на складе"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
