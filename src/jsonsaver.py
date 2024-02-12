class JSONSaver:
    """Класс для хранения информации о вакансиях в JSON-файле."""

    def __init__(self, file_name='vacancies.json'):
        """
        Создание экземпляра класса JSONSaver.
        :param file_name: название JSON-файла, по умолчанию 'vacancies.json'.
        """
        self.file_name = file_name
