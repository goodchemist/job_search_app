import json


class JSONSaver:
    """Класс для хранения информации о вакансиях в JSON-файле."""

    def __init__(self, file_name='vacancies.json'):
        """
        Создание экземпляра класса JSONSaver.
        :param file_name: название JSON-файла, по умолчанию 'vacancies.json'.
        """
        self.file_name = file_name

    def save_to_json(self, vacancies):
        """
        Запись информации о вакансиях в JSON-файл.
        :param vacancies: информация о вакансиях.
        """
        vacancy_list = []

        for vacancy in vacancies:
            vacancy_dict = vacancy.__dict__
            vacancy_list.append(vacancy_dict)

        with open(self.file_name, 'w') as file:
            json.dump(vacancy_list, file, ensure_ascii=False, indent=4)  # без использования кодировки ASCII + отступы

    def clear_json_file(self):
        """
        Очистка JSON-файла.
        """
        with open(self.file_name, 'w') as file:
            file.truncate(0)  # обрезаем файл до 0 байт

    def add_to_json_file(self, vacancy):
        """
        Добавление одной вакансии в JSON-файл.
        :param vacancy: информация об одной вакансии.
        """
        with open(self.file_name, 'r') as file:
            current_data = json.load(file)

        current_data.append(vacancy)

        with open(self.file_name, 'w') as file:
            json.dump(current_data, file)
