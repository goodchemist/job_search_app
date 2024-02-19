from abc import ABC, abstractmethod


class Saver(ABC):
    """
    Абстрактный класс для хранения информации в JSON-файле.
    """

    @abstractmethod
    def save_to_json(self, data):
        """
        Запись информации в JSON-файл.
        :param data: информация.
        """
        pass

    @abstractmethod
    def clear_json_file(self):
        """
        Очистка JSON-файла.
        """
        pass

    @abstractmethod
    def add_to_json_file(self, data):
        """
        Добавление информации в JSON-файл.
        :param data: информация.
        """
        pass
