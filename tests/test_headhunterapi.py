import pytest
from src.headhunterapi import HeadHunterAPI


def test_get_vacancies_valid_query():
    """
    Проверяет корректный результат для действительного запроса.
    """
    api = HeadHunterAPI()

    query = "python"

    data_json = api.get_vacancies(query)

    assert data_json is not None


def test_get_vacancies_invalid_query():
    """
    Проверяет, что вызов метода с недопустимым запросом вызовет исключение ValueError.
    """
    api = HeadHunterAPI()

    query = ""

    with pytest.raises(ValueError):
        api.get_vacancies(query)


def test_get_vacancies_exception():
    """
    Проверяет вызов исключения при возникновении ошибки запроса.
    """
    with pytest.raises(Exception) as exc:
        fake_api = HeadHunterAPI()

        fake_api._url = 'https://fakeapi.hh.ru/vacancies'

        fake_api.get_vacancies('test')

    assert str(
        exc.value) == (f'Ошибка при выполнении запроса: 404 Client Error: Not Found for url: \
{fake_api._url + "?text=test&per_page=100"}.')


def test_repr():
    """
    Проверяет корректность метода __repr__.
    """
    api = HeadHunterAPI()

    representation = repr(api)

    assert representation == "HeadHunterAPI(data_json=None)"


def test_str():
    """
    Проверяет корректность метода __str__.
    """
    api = HeadHunterAPI()

    representation = str(api)

    assert representation == 'None'
