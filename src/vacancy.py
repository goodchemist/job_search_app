class Vacancy:
    """Класс для работы с вакансиями."""

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

    def __str__(self) -> str:
        """
        Метод для отображения экземпляра класса Vacancy.
        :return: f-строка с данными экземпляра Vacancy.
        """
        return (f'{self.name}, {self.salary_from}, {self.salary_to}, {self.salary_currency}, {self.city}, '
                f'{self.description}, {self.url_vacancy}')

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса Vacancy.
        :return: f-строка с данными экземпляра Vacancy.
        """
        return (f'Vacancy(name={self.name}, salary_from={self.salary_from}, salary_to={self.salary_to}, '
                f'salary_currency={self.salary_currency}, city={self.city}, description={self.description}, '
                f'url_vacancy={self.url_vacancy})')
