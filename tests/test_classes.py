from src.main import Category


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


def test_init_category(category_data):
    assert category_data.name == "Смартфоны"
    assert category_data.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных " "функций для удобства жизни"
    )
    assert len(category_data.products) == 3

    assert Category.category_count == 1
    assert category_data.category_count == 1
    assert Category.product_count == 3
