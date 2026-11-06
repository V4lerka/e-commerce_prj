import json
from unittest.mock import mock_open, patch

from src.utils import do_objects_from_data, read_json


def test_read_json(capsys):
    """Неверное расширение"""
    result = read_json("products.txt")
    captured = capsys.readouterr()
    assert result == []
    assert captured.out == "Ошибка: неверное расширение файла. Невозможно прочитать файл.\n"


def test_read_json2(read_json_test_data):
    """Успешный тест"""
    file_content = json.dumps(read_json_test_data)
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file), patch("os.path.abspath", return_value="/fake/path/fake.json"):
        result = read_json("fake.json")
    assert result == read_json_test_data


def test_read_json3(capsys):
    """Тест с пустым файлом, ошибка чтения"""
    file_content = ""
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file), patch("os.path.abspath", return_value="/fake/path/fake.json"):
        result = read_json("fake.json")
    captured = capsys.readouterr()
    assert result == []
    assert captured.out == "Ошибка чтения файла: Expecting value: line 1 column 1 (char 0)\n"


def test_read_json4(capsys):
    """Тест, если файл не найден"""

    def mock_open_raise_error(*args, **kwargs):
        raise FileNotFoundError("[Errno 2] No such file or directory")

    with (
        patch("builtins.open", mock_open_raise_error),
        patch("os.path.abspath", return_value="/fake/path/missing.json"),
    ):
        result = read_json("missing.json")
    assert result == []
    captured = capsys.readouterr()
    assert "Ошибка: [Errno 2] No such file or directory" in captured.out


def test_do_objects_from_data(capsys):
    """Тест с пустым списком"""
    result = do_objects_from_data([])
    captured = capsys.readouterr()
    assert result == []
    assert captured.out == "Данные отсутствуют\n"


def test_do_objects_from_data2(test_data_utils):
    """Успешный тест"""
    result = do_objects_from_data(test_data_utils)
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert len(result) == 2
