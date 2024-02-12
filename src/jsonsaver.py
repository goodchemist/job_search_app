import json


class JSONSaver:
    """Класс для хранения информации о вакансиях в JSON-файле."""

    def __init__(self, file_name='vacancies.json'):
        """
        Создание экземпляра класса JSONSaver.
        :param file_name: название JSON-файла, по умолчанию 'vacancies.json'.
        """
        self.file_name = file_name

    def save_to_json(self, data):
        """
        Запись информации о вакансиях в JSON-файл.
        :param data: информация о вакансиях.
        """
        with open(self.file_name, 'w') as file:
            json.dump(data, file)
