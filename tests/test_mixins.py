from src.classes import Product
from src.subclasses import Smartphone, LawnGrass


def test_mixin(capsys):
    """Тест работы миксин-класса (вывод в консоль) на Продукте и дочерних классах"""

    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message1 = capsys.readouterr()
    assert message1.out == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message2 = capsys.readouterr()
    assert message2.out == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message3 = capsys.readouterr()
    assert message3.out == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)\n"
