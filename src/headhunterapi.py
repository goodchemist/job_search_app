import requests

from abstract_searchjobapi import SearchJobAPI


class HeadHunterAPI(SearchJobAPI):
    """
    Класс для работы с API платформы HeadHunter с вакансиями.
    """

    def __init__(self):
        """
        Создание экземпляра класса, где в data_json будут хранится полученные данные в json формате.
        """
        self.data_json = None

    def get_vacancies(self, query: str):
        """
        Метод, для получения вакансий с hh.ru в формате json.

        :param query: Поисковый запрос.
        :return: Вакансии в формате json.
        """

        url = 'https://api.hh.ru/vacancies'

        if isinstance(query, str):
            query_ = {'text': query}

        else:
            raise ValueError('Запрос составлен не корректно... :(')

        response = requests.get(url, params=query_)

        if response.status_code == 200:

            self.data_json = response.json()

            return self.data_json

        raise Exception('О нет, что-то пошло не так. Попробуй позже.')

    def __str__(self):
        """
        Метод для отображения экземпляра класса HeadHunterAPI.
        :return: f-строка.
        """
        return f'{self.data_json}'

    def __repr__(self):
        pass
