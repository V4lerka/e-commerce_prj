# Проект "E-commerce"🧑‍💻
___
## Содержание🗃️
- [Описание](#описание)
- [Требования](#требования)
- [Использование](#использование)
- [Описание функционала](#описание-функционала)
- [Запуск](#запуск)
- [Лицензия](#лицензия)
- [Команда проекта ](#команда-проекта-)
- [Источники](#источники)
- [Тестирование](#тестирование-)  
___
## Описание🪪
**Приложение для онлайн-магазина.**  

[[*к содержанию*⤴️]](#содержание)
___
## Требования📝
Для работы с проектом вам понадобится установить на свой ПК следующее:

[![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![PyCharm](https://img.shields.io/badge/pycharm-%23000000.svg?style=for-the-badge&logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)  

[[*к содержанию*⤴️]](#содержание)
___
## Использование🛠️
* Клонируйте репозиторий: `https://github.com/V4lerka/e-commerce_prj.git`
* Установите зависимости из **pyproject.toml**: `poetry install`
* При необходимости обновите зависимости: `poetry update`  

[[*к содержанию*⤴️]](#содержание)
___
## Описание функционала:🪄
* Модуль **classes.py** содержит классы "Product", "Category", "CategoryIterator", "Order", а также абстрактный класс 
"BaseProduct".
* Модуль **utils.py** содержит функцию для чтения JSON-файла и создания объектов класса из полученных данных.
* Модуль **subclasses.py** содержит подклассы "Smartphone" и "LawnGrass" (производные от "Product").
* Модуль **mixins.py** содержит дополнительные классы для расширения функционала.
  
[[*к содержанию*⤴️]](#содержание)
___
## Запуск🚀
- Запускаем команду в терминале `python -m src.utils`.
- Запускаем команду в терминале `python -m src.main`.

[[*к содержанию*⤴️]](#содержание)
___
## Лицензия🔐
MIT🆓 😂  
[[*к содержанию*⤴️]](#содержание)
___
## Команда проекта 🤝
[Valerii Dutov](https://github.com/V4lerka/V4lerka) — Начинающий Python-разработчик  

[[*к содержанию*⤴️]](#содержание)
___
## Источники📚📻📺
[Вдохновение для этого файла](https://github.com/GnuriaN/format-README/blob/master/README.md#%D0%9E%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  

[[*к содержанию*⤴️]](#содержание)

## Тестирование🧑‍🦽‍➡️  
| File               | statements | missing | excluded | coverage |
|--------------------|------------|---------|----------|----------|
| src\__init__.py    | 0          | 0       | 0        | 100 %    |
| src\classes.py     | 88         | 8       | 0        | 91 %     |
| src\mixins.py      | 5          | 0       | 0        | 100 %    |
| src\main.py        | 82         | 79      | 0        | 4 %      |
| src\subclasses.py  | 24         | 0       | 0        | 100 %    |
| src\utils.py       | 41         | 7       | 0        | 83 %     |
| **Total**          | **158**    | **15**  | **0**    | **91 %** |