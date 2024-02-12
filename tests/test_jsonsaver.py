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


def test_clear_json_file(file_name):
    """
    Проверяет работу метода clear_json_file.
    """
    json_saver = JSONSaver(file_name)  # создаем экземпляр JSONSaver

    # записывае тестовые данные
    with open(file_name, "w") as file:
        file.write("some data")

    json_saver.clear_json_file()  # очищаем файл

    # проверяем пустой ли файл
    with open(file_name, "r") as file:
        assert file.read() == ""


def test_add_to_json_file(file_name):
    """
    Проверяет работу метода add_to_json_file.
    """
    json_saver = JSONSaver(file_name)  # создаем экземпляр JSONSaver

    test_data = [{"name": "Alice", "age": 25}]  # тестовые данные
    json_saver.save_to_json(test_data)  # сохраняем данные в JSON-файл

    new_data = {"name": "Bob", "age": 30}  # новые тестовые данные
    json_saver.add_to_json_file(new_data)  # добавляем новые тестовые данные

    # проверяем записались ли в файл новые тестовые данные
    with open(file_name, "r") as file:
        data = json.load(file)
        assert len(data) == 2
        assert data[1] == new_data
