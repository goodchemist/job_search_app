class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, name: str, salary_from: (int | float | str), salary_to: (int | float | str),
                 salary_currency: str, city: str, description: str,
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
        self.salary_from = salary_from
        self.salary_to = salary_to
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

    @classmethod
    def cast_to_object_list(cls, json_data) -> list:
        """
        Преобразует набор данных из JSON в список объектов.
        :param json_data: JSON с информацией о вакансиях.
        :return: список с вакансиями.
        """
        vacancies = []

        for vacancy_data in json_data['items']:
            name = vacancy_data['name']

            try:
                salary_from = vacancy_data['salary']['from']
            except TypeError:
                salary_from = '--'

            if salary_from is None:
                salary_from = '--'

            try:
                salary_to = vacancy_data['salary']['to']
            except TypeError:
                salary_to = '--'

            if salary_to is None:
                salary_to = '--'

            try:
                salary_currency = vacancy_data['salary']['currency']
            except TypeError:
                salary_currency = 'Валюта не указана'

            if salary_currency is None:
                salary_currency = 'Валюта не указана'

            city = vacancy_data['area']['name']
            description = vacancy_data['snippet']['responsibility']
            url_vacancy = vacancy_data['alternate_url']

            vacancy = cls(
                name,
                salary_from,
                salary_to,
                salary_currency,
                city,
                description,
                url_vacancy
            )

            vacancies.append(vacancy)

        return vacancies

    @staticmethod
    def calculate_max_salary(vacancy) -> int | float:
        """
        Метод для расчета большего значения зарплаты из диапазона 'от'-'до', если они указаны.
        :param vacancy: экземпляр класса Vacancy.
        :return: большее значение диапазона зарплаты.
        """
        if vacancy.salary_to == '--':
            if vacancy.salary_from == '--':
                return 0
            elif isinstance(vacancy.salary_from, (int, float)):
                return vacancy.salary_from

        elif vacancy.salary_from == '--':
            if isinstance(vacancy.salary_to, (int, float)):
                return vacancy.salary_to

        else:
            return max(vacancy.salary_to, vacancy.salary_from)

    @classmethod
    def sort_by_salary(cls, vacancies: list) -> list:
        """
        Сортирует вакансии по зарплате, от большей к наименьшей.
        :param vacancies: список с вакансиями.
        :return: отсортированный список вакансий по зарплате.
        """

        sorted_vacancies = sorted(vacancies,
                                  key=lambda vacancy: (cls.calculate_max_salary(vacancy), vacancy.salary_currency),
                                  reverse=True)
        return sorted_vacancies

    @classmethod
    def get_top_n_vacancies_by_salary(cls, vacancies: list, top_n: int) -> list:
        """
        Сохраняет только по top_n вакансии с максимальной зарплатой в каждой категории salary_currency.
        Если в категории меньше top_n то сколько есть.
        :param vacancies: список вакансий.
        :param top_n: количество вакансий для вывода в топ.
        :return: список вакансий с максимальной зарплатой в соответствующей валюте.
        """

        sorted_vacancies = cls.sort_by_salary(vacancies)

        top_vacancies = {}

        for vacancy in sorted_vacancies:

            salary_currency = vacancy.salary_currency

            if salary_currency == 'Валюта не указана':
                continue

            if salary_currency not in top_vacancies:
                top_vacancies[salary_currency] = []

            else:
                if len(top_vacancies[salary_currency]) >= top_n:
                    continue

                else:
                    top_vacancies[salary_currency].append(vacancy)

        top_vacancies_list = []

        for currency, vacancies in top_vacancies.items():
            top_vacancies_list.extend(vacancies)

        return top_vacancies_list

    @classmethod
    def get_vacancies_by_city(cls, vacancies: list, city: str) -> list:
        """
        Находит вакансии из списка вакансий по указанному городу.
        :param vacancies: список вакансий.
        :param city: название города.
        :return: список вакансий в указанном городе.
        """
        vacancies_by_city = []

        for vacancy in vacancies:
            if vacancy.city.lower() == city.lower():
                vacancies_by_city.append(vacancy)

        return vacancies_by_city
