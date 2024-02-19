import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    """
    Фикстура для создания экземпляра класса Vacancy.
    """
    return Vacancy(name='Software Engineer', salary_from=50000, salary_to=80000,
                   salary_currency='RUR', city='Moscow', description='Python developer',
                   url_vacancy='www.hh.ru')


def test_vacancy_initialization(vacancy):
    """
    Проверяет работу __init__.
    """
    assert vacancy.name == 'Software Engineer'
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 80000
    assert vacancy.salary_currency == 'RUR'
    assert vacancy.city == 'Moscow'
    assert vacancy.description == 'Python developer'
    assert vacancy.url_vacancy == 'www.hh.ru'


def test_calculate_max_salary_when_both_salaries_provided(vacancy):
    """
    Проверяет работу метода calculate_max_salary, когда указаны salary_to, salary_from.
    """
    assert Vacancy.calculate_max_salary(vacancy) == 80000


def test_calculate_max_salary_when_only_salary_from_provided(vacancy):
    """
    Проверяет работу метода calculate_max_salary, когда не указана salary_to.
    """
    vacancy.salary_to = '--'
    assert Vacancy.calculate_max_salary(vacancy) == 50000


def test_calculate_max_salary_when_only_salary_to_provided(vacancy):
    """
    Проверяет работу метода calculate_max_salary, когда не указана salary_from.
    """
    vacancy.salary_from = '--'
    assert Vacancy.calculate_max_salary(vacancy) == 80000


def test_calculate_max_salary_when_both_salaries_not_provided(vacancy):
    """
    Проверяет работу метода calculate_max_salary, когда указаны не salary_to, salary_from.
    """
    vacancy.salary_from = '--'
    vacancy.salary_to = '--'
    assert Vacancy.calculate_max_salary(vacancy) == 0
