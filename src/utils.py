import json
import os
from json import JSONDecodeError
from typing import Any

from src.classes import Category, Product


def read_json(filename: str) -> list[Any]:
    """Функция, которая будет читать файл JSON и возвращать список словарей."""
    full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data", f"{filename}"))
    if filename.endswith("json"):
        try:
            with open(full_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError as e:
            print(f"Ошибка: {e}")
            return []
        except JSONDecodeError as e:
            print(f"Ошибка чтения файла: {e}")
            return []
    print("Ошибка: неверное расширение файла. Невозможно прочитать файл.")
    return []


def do_objects_from_data(data: list) -> list[Any]:
    """Функция принимает список словарей и возвращает список объектов класса"""
    if data:
        categories_list = []
        for category in data:
            product_list = []
            if category.get("products"):
                for product in category["products"]:
                    product_list.append(Product(**product))
                category["products"] = product_list
                categories_list.append(Category(**category))
        return categories_list
    print("Данные отсутствуют")
    return []


if __name__ == "__main__":
    list_ctgs = read_json("products.json")
    categories_data = do_objects_from_data(list_ctgs)
    print(categories_data)
    print(categories_data[0].name)
    print(categories_data[1].name)
    print(categories_data[0].products)
    print(categories_data[1].products)
