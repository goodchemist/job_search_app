import json

import pytest
from src.jsonsaver import JSONSaver


@pytest.fixture
def file_name(tmp_path):
    """
     Фикстура для создания временного файла 'test_file.json'.
    :param tmp_path: указывает путь временного каталога, где содержится тестовый файл.
    """
    return tmp_path / "test_file.json"


def test_save_to_json(file_name):
    """
    Проверяет работу метода save_to_json.
    """
    json_saver = JSONSaver(file_name)  # создаем экземпляр JSONSaver

    test_data = {"name": "Alice", "age": 25}  # тестовые данные
    json_saver.save_to_json(test_data)  # сохраняем данные в JSON-файл

    assert file_name.is_file()  # проверяем создан ли файл

    with open(file_name, "r") as file:
        data = json.load(file)
        assert data == test_data  # совпадают ли данные в файле с тестовыми данными
