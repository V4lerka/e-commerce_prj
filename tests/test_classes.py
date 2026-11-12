from unittest.mock import patch

import pytest

from src.classes import BaseProduct
from src.main import Category, Product
from src.mixins import MixinPrinter
from src.classes import Order

def test_init_product(product_data1, product_data2, product_data3):
    assert product_data1.name == "Samsung Galaxy S23 Ultra"
    assert product_data1.description == "256GB, Серый цвет, 200MP камера"
    assert product_data1.price == 180000
    assert product_data1.quantity == 5
    assert product_data2.name == "Iphone 15"
    assert product_data2.description == "512GB, Gray space"
    assert product_data2.price == 210000.0
    assert product_data2.quantity == 8
    assert product_data3.name == "Xiaomi Redmi Note 11"
    assert product_data3.description == "1024GB, Синий"
    assert product_data3.price == 31000.0
    assert product_data3.quantity == 14


def test_init_product_zero_quantity():
    """Создание товара с нулевым количеством"""

    with pytest.raises(ValueError) as e:
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"


def test_init_category(category_data):
    assert category_data.name == "Смартфоны"
    assert category_data.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных " "функций для удобства жизни"
    )
    assert category_data.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n\
Iphone 15, 210000.0 руб. Остаток: 8 шт.\n\
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."

    assert Category.category_count == 1
    assert category_data.category_count == 1
    assert Category.product_count == 3


def test_add_product_ok(category_data, product_data1):
    category_data.add_product(product_data1)
    assert category_data.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n\
Iphone 15, 210000.0 руб. Остаток: 8 шт.\n\
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n\
Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product_error(category_data):
    with pytest.raises(TypeError) as e:
        category_data.add_product("Товар категории Х")
    assert str(e.value) == "Можно добавить только объект класса Продукт или дочернего класса"


def test_new_product(new_product_data):
    """Тест, если продукта нет в списке"""
    new_prod = Product.new_product(new_product_data, [])
    assert new_prod.name == "Iphone 18"
    assert new_prod.description == "512GB, Red space"
    assert new_prod.price == 210000.0
    assert new_prod.quantity == 18


def test_new_product2(product_data1, product_data2, product_data3, new_product_test_data):
    """Тест, если продукт есть в списке, но у него другая цена"""
    list_prods = [product_data1, product_data2, product_data3]
    new_prod = Product.new_product(new_product_test_data, list_prods)
    assert new_prod is None
    assert product_data2.quantity == 26
    assert product_data2.price == 250000.0


def test_price_setter_higher(product_data1):
    """Тест новой цены, выше прежней"""
    assert product_data1.price == 180_000
    product_data1.price = 210_000
    assert product_data1.price == 210_000


def test_price_setter_lower(product_data1):
    """Тест новой цены ниже прежней"""
    assert product_data1.price == 180_000
    with patch("builtins.input", return_value="y"):
        product_data1.price = 100_000
    assert product_data1.price == 100_000


def test_price_setter_lower2(product_data1):
    """Тест новой цены ниже прежней"""
    assert product_data1.price == 180_000
    with patch("builtins.input", return_value="n"):
        product_data1.price = 100_000
    assert product_data1.price == 180_000


def test_price_setter_zero(product_data1, capsys):
    """Тест цены 0"""
    assert product_data1.price == 180_000
    product_data1.price = 0
    assert product_data1.price == 180_000
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_str_product(product_data1):
    assert str(product_data1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(category_data):
    assert str(category_data) == "Смартфоны, количество продуктов: 27 шт."


def test_dunder_add_ok(product_data1, product_data2, product_data3):
    result1_2 = product_data1 + product_data2
    result2_3 = product_data2 + product_data3
    result_all = result1_2 + product_data3
    assert result1_2.name == "Samsung Galaxy S23 Ultra+Iphone 15"
    assert result1_2.price == 2580000.0
    assert result2_3.name == "Iphone 15+Xiaomi Redmi Note 11"
    assert result2_3.price == 2114000.0
    assert result_all.price == 3014000.0


def test_dunder_add_error(product_data1):
    with pytest.raises(TypeError):
        result = product_data1 + "Товар"
        print(result)


def test_category_iterator(category_iterator):
    assert category_iterator.index == 0
    assert next(category_iterator) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert next(category_iterator) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert next(category_iterator) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    with pytest.raises(StopIteration):
        next(category_iterator)


def test_product_is_subclass_base_class(product_data1, smartphone1):
    """Проверка наследования базового класса BaseProduct"""
    assert isinstance(product_data1, BaseProduct) is True
    assert isinstance(smartphone1, BaseProduct) is True


def test_product_is_subclass_mixin(product_data1, smartphone1):
    """Проверка наследования миксин-класса"""
    assert isinstance(product_data1, MixinPrinter) is True
    assert isinstance(smartphone1, MixinPrinter) is True


def test_middle_price_ok(category_data):
    """Успешный тест функции"""
    assert category_data.middle_price() == 140333.3


def test_middle_price_empty(capsys):
    """Тест с пустым списком"""
    empty_cat = Category("Пустая категория", "Категория без продуктов", [])
    assert empty_cat.middle_price() == 0
    message = capsys.readouterr()
    assert message.out == "Ошибка: расчет не возможен! Список товаров категории пуст\n"


def test_middle_price_wrong_price(category_data2, capsys):
    """Тест если цена не указана или ее формат неверный"""

    assert category_data2.middle_price() == 0
    message = capsys.readouterr()
    assert message.out == "Ошибка: расчет не возможен! Для одного или нескольких товаров не указана цена \
или неверный формат данных\n"

def test_middle_price_wrong_price2(category_data3, capsys):
    """Тест если цена не указана или ее формат неверный"""

    assert category_data3.middle_price() == 0
    message = capsys.readouterr()
    assert message.out == "Ошибка: расчет не возможен! Для одного или нескольких товаров не указана цена \
или неверный формат данных\n"


def test_init_order(product_data1):
    """Тест инициализации заказа при количестве 0"""
    with pytest.raises(ValueError, match="Количество заказываемого товара не может быть отрицательным или нулевым"):
        Order(product_data1, 0)


def test_init_order2(product_data1):
    """Тест инициализации заказа при количестве большем, чем есть"""
    with pytest.raises(ValueError, match="Недостаточно товара 'Samsung Galaxy S23 Ultra'. Доступно: 5 шт."):
        Order(product_data1, 7)


def test_init_order3(product_data1):
    """Успешная инициализация заказа"""
    assert product_data1.quantity == 5
    Order(product_data1, 1)
    product_data1.product = product_data1
    product_data1.amount_ordered = 1
    assert product_data1.product.quantity == 4


def test_calculate_price_order(product_data1):
    """Тест определения стоимости заказа"""
    my_order = Order(product_data1, 1)
    assert my_order.calculate_total_price() == 180000
