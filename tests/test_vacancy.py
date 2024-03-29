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


@pytest.fixture
def vacancies():
    """
    Фикстура со списком вакансий (экземпляров класса Vacancy).
    """
    vacancies = [
        Vacancy(name='A-RUR', salary_from=50000, salary_to=80000, salary_currency='RUR', city='Moscow',
                description='--', url_vacancy='123'),
        Vacancy(name='B-RUR', salary_from=60000, salary_to=90000, salary_currency='RUR', city='New York',
                description='--', url_vacancy='123'),
        Vacancy(name='C-RUR', salary_from=55000, salary_to=85000, salary_currency='RUR', city='Seattle',
                description='--', url_vacancy='123'),
        Vacancy(name='A-USD', salary_from=500, salary_to=800, salary_currency='USD', city='Moscow', description='--',
                url_vacancy='123'),
        Vacancy(name='B-USD', salary_from=600, salary_to=900, salary_currency='USD', city='New York', description='--',
                url_vacancy='123'),
        Vacancy(name='C-USD', salary_from=550, salary_to=850, salary_currency='USD', city='Seattle', description='--',
                url_vacancy='123')
    ]

    return vacancies


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


def test_sort_by_salary(vacancies):
    """
    Проверяет работу метода sort_by_salary.
    """

    sorted_vacancies = Vacancy.sort_by_salary(vacancies)

    assert sorted_vacancies[0].name == 'B-RUR'
    assert sorted_vacancies[1].name == 'C-RUR'
    assert sorted_vacancies[2].name == 'A-RUR'
    assert sorted_vacancies[3].name == 'B-USD'
    assert sorted_vacancies[4].name == 'C-USD'
    assert sorted_vacancies[5].name == 'A-USD'


def test_get_top_n_vacancies_by_salary(vacancies):
    """
    Проверяет работу метода get_top_n_vacancies_by_salary.
    """

    top_n = 2

    top_vacancies = Vacancy.get_top_n_vacancies_by_salary(vacancies, top_n)
    assert len(top_vacancies) == 4  # т.к. у нас останется 2 вакансии c RUR и 2 вакансии c USD


def test_get_vacancies_by_city(vacancies):
    """
    Проверяет работу метода get_vacancies_by_city.
    """

    city = 'Moscow'

    vacancies_in_city = Vacancy.get_vacancies_by_city(vacancies, city)

    for vacancy in vacancies_in_city:
        assert vacancy.city.lower() == city.lower()


def test_str(vacancy):
    """
    Проверяет корректность метода __str__.
    """

    assert str(vacancy) == 'Software Engineer, 50000, 80000, RUR, Moscow, Python developer, www.hh.ru'


def test_repr(vacancy):
    """
    Проверяет корректность метода __repr__.
    """
    representation = 'Vacancy(name=Software Engineer, salary_from=50000, salary_to=80000, salary_currency=RUR, \
city=Moscow, description=Python developer, url_vacancy=www.hh.ru)'

    assert repr(vacancy) == representation


def test_cast_to_object_list():
    """
    Проверяет работу метода cast_to_object_list.
    """
    json_data = {
        'items': [
            {'name': 'Python development', 'salary': {'from': 50000, 'to': 80000, 'currency': 'RUR'},
             'area': {'name': 'Omsk'}, 'snippet': {'responsibility': 'abc'}, 'alternate_url': '123'},
            {'name': 'Product Manager', 'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR'},
             'area': {'name': 'Moscow'}, 'snippet': {'responsibility': 'abc'}, 'alternate_url': '123'}
        ]
    }

    vacancies = Vacancy.cast_to_object_list(json_data)

    assert len(vacancies) == 2
    assert vacancies[0].name == 'Python development'
    assert vacancies[0].salary_from == 50000
    assert vacancies[1].city == 'Moscow'


def test_cast_to_object_list_with_no_salary():
    """
    Проверяет работу метода cast_to_object_list, если нет никаких данных по зарплате.
    """
    json_data = {
        'items': [
            {'name': 'Python development', 'salary': None,
             'area': {'name': 'Omsk'}, 'snippet': {'responsibility': 'abc'}, 'alternate_url': '123'},
        ]
    }
    vacancies = Vacancy.cast_to_object_list(json_data)

    assert vacancies[0].salary_from == '--'
    assert vacancies[0].salary_to == '--'
    assert vacancies[0].salary_currency == 'Валюта не указана'


def test_cast_to_object_list_with_valid_salary():
    """
    Проверяет работу метода cast_to_object_list, если какие-то данные по зарплате не указаны.
    """
    json_data = {
        'items': [
            {'name': 'Python development', 'salary': {'from': None, 'to': None, 'currency': None},
             'area': {'name': 'Omsk'}, 'snippet': {'responsibility': 'abc'}, 'alternate_url': '123'},
        ]
    }
    vacancies = Vacancy.cast_to_object_list(json_data)

    assert vacancies[0].salary_from == '--'
    assert vacancies[0].salary_to == '--'
    assert vacancies[0].salary_currency == 'Валюта не указана'
