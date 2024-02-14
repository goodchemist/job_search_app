import json
import pytest

from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def file_name(tmp_path):
    """
     Фикстура для создания временного файла 'test_file.json'.
    :param tmp_path: указывает путь временного каталога, где содержится тестовый файл.
    """
    return tmp_path / "test_file.json"


@pytest.fixture
def test_data():
    data = [
        Vacancy('name_1', '0', '1', 'RUR', 'A', '-', '-'),
        Vacancy('name_2', '0', '2', 'USD', 'B', '-', '-')
    ]
    return data


def test_save_to_json(file_name, test_data):
    """
    Проверяет работу метода save_to_json.
    """
    json_saver = JSONSaver(file_name)  # создаем экземпляр JSONSaver

    json_saver.save_to_json(test_data)  # сохраняем данные в JSON-файл

    assert file_name.is_file()  # проверяем создан ли файл

    with open(file_name, "r") as file:
        data = json.load(file)
        assert data[0]["name"] == "name_1"
        assert data[1]["salary_to"] == "2"  # совпадают ли данные в файле с тестовыми данными


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


def test_add_to_json_file(file_name, test_data):  # !!!!!
    """
    Проверяет работу метода add_to_json_file.
    """
    json_saver = JSONSaver(file_name)  # создаем экземпляр JSONSaver

    json_saver.save_to_json(test_data)  # сохраняем данные в JSON-файл

    for data in test_data:
        json_saver.add_to_json_file(data)  # добавляем еще тестовые данные

    # проверяем записались ли в файл новые тестовые данные
    with open(file_name, "r") as file:
        data = json.load(file)
        assert len(data) == 4
        assert data[3]["salary_to"] == "2"
