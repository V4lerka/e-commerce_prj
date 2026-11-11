import pytest


def test_init_smartphone(smartphone1):
    """Тест инициализации подкласса Смартфоны"""

    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_init_lawn_grass(lawn_grass1):
    """Тест инициализации подкласса Газонная трава"""

    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_add_smartphone_ok(smartphone1, smartphone2):
    """Тест сложения смартфонов"""

    result = smartphone1 + smartphone2
    assert result.name == "Samsung Galaxy S23 Ultra+Iphone 15"
    assert result.price == 2580000.0
    assert result.description == "Сумма"
    assert result.quantity == 1
    assert result.efficiency is None
    assert result.model is None
    assert result.memory is None
    assert result.color is None


def test_add_lawn_grass_ok(lawn_grass1, lawn_grass2):
    """Тест сложения газонной травы"""

    result = lawn_grass1 + lawn_grass2
    assert result.name == "Газонная трава+Газонная трава 2"
    assert result.description == "Сумма"
    assert result.price == 16750.0
    assert result.quantity == 1
    assert result.country is None
    assert result.germination_period is None
    assert result.color is None


def test_add_lawn_grass_error(lawn_grass1):
    """Сложение разных типов данных"""

    with pytest.raises(TypeError) as e:
        result = lawn_grass1 + 23
        print(result)
    assert str(e.value) == "Можно складывать данные только одного класса"


def test_add_smartphone_error(smartphone1):
    """Сложение разных типов данных"""

    with pytest.raises(TypeError) as e:
        result = smartphone1 + "Смартфон"
        print(result)
    assert str(e.value) == "Можно складывать данные только одного класса"
