class Vacancy:
    """
    Класс для работы с вакансиями.
    """
    def __init__(self, name: str, salary_from: str, salary_to: str, salary_currency: str, city: str, description: str,
                 url_vacancy: str) -> None:
        """
        Создание экземпляра класса Vacancy.
        :param name: наименование вакансии.
        :param salary_from: зарплата от.
        :param salary_to: зарплата до.
        :param salary_currency: валюта.
        :param city: город.
        :param description: описание вакансии.
        :param url_vacancy: ссылка на вакансию.
        """
        self.name = name
        self.salary_from = int(salary_from)
        self.salary_to = int(salary_to)
        self.salary_currency = salary_currency
        self.city = city
        self.description = description
        self.url_vacancy = url_vacancy
