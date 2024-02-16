import requests

from .abstract_searchjobapi import SearchJobAPI


class HeadHunterAPI(SearchJobAPI):
    """Класс для работы с API платформы HeadHunter с вакансиями."""

    def __init__(self) -> None:
        """
        Создание экземпляра класса, где в data_json будут хранится полученные данные в JSON формате.
        """
        self.data_json = None
        self._url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, query: str) -> dict:
        """
        Метод для получения вакансий с hh.ru в формате JSON.
        :param query: Поисковый запрос.
        :return: Вакансии в формате JSON.
        """
        if not isinstance(query, str) or not query:
            raise ValueError('Поисковый запрос должен быть непустой строкой.')

        query_ = {'text': query, 'per_page': 100}

        try:
            response = requests.get(self._url, params=query_)

            response.raise_for_status()  # Вызов исключения для кодов статуса 4xx/5xx

            self.data_json = response.json()
            return self.data_json

        except requests.exceptions.RequestException as e:
            raise Exception(f'Ошибка при выполнении запроса: {e}.')

    def __str__(self) -> str:
        """
        Метод для отображения экземпляра класса HeadHunterAPI.
        :return: f-строка с данными в формате JSON из атрибута data_json.
        """
        return f'{self.data_json}'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса HeadHunterAPI.
        :return: f-строка с данными в формате JSON из атрибута data_json.
        """
        return f'HeadHunterAPI(data_json={self.data_json})'
