from abc import ABC, abstractmethod


class SearchJobAPI(ABC):
    """
    Абстрактный класс для работы с API платформ с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, query):
        """
        Метод, для получения вакансий с hh.ru в формате json.

        :param query: Поисковый запрос.
        :return: Вакансии в формате json.
        """
        pass
