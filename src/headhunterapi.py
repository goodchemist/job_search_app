import requests

from abstract_searchjobapi import SearchJobAPI


class HeadHunterAPI(SearchJobAPI):
    """Класс для работы с API платформы HeadHunter с вакансиями."""

    def __init__(self):
        """
        Создание экземпляра класса, где в data_json будут хранится полученные данные в JSON формате.
        """
        self.data_json = None

    def get_vacancies(self, query: str):
        """
        Метод для получения вакансий с hh.ru в формате JSON.
        :param query: Поисковый запрос.
        :return: Вакансии в формате JSON.
        """
        if not isinstance(query, str) or not query:
            raise ValueError('Поисковый запрос должен быть непустой строкой.')

        url = 'https://api.hh.ru/vacancies'

        query_ = {'text': query}

        try:
            response = requests.get(url, params=query_)

            response.raise_for_status()  # Вызов исключения для кодов статуса 4xx/5xx

            self.data_json = response.json()
            return self.data_json

        except requests.exceptions.RequestException as e:
            raise Exception(f'Ошибка при выполнении запроса: {e}.')

    def __str__(self):
        """
        Метод для отображения экземпляра класса HeadHunterAPI.
        :return: f-строка с данными в формате JSON из атрибута data_json.
        """
        return f'{self.data_json}'

    def __repr__(self):
        """
        Возвращает строковое представление экземпляра класса HeadHunterAPI.
        :return: f-строка с данными в формате JSON из атрибута data_json.
        """
        return f'HeadHunterAPI(data_json={self.data_json})'
