import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
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
