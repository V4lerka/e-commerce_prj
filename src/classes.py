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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        list_products = [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in
                         self.__products]
        return "\n".join(list_products)
