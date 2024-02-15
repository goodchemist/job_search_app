from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy


def save_vacancies(vacancies: list) -> None:
    """
    Спрашивает у пользователя сохранить ли вакансии в файл, выполняет нужное действие.
    :param vacancies: список с вакансиями.
    :return: None.
    """
    while True:
        user_input = input("Сохранить вакансии в файл?\n(0 - да, 1 - нет)").strip()

        if user_input == '0':
            json_saver = JSONSaver()
            json_saver.save_to_json(vacancies)
            break

        elif user_input == '1':
            break

        else:
            print("Попробуйте еще раз.")
            continue


# Функция для взаимодействия с пользователем
def user_interaction():
    # Пользователь вводит ключевое слово
    search_query = input("Привет, я помогу тебе найти работу! :)\nВведите ключевое слово для поиска: ").strip().lower()

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение нужных вакансий с HH.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразует набор данных из JSON в список объектов класса Vacancy
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Цикл для выбора нужного варианта пользователем
    while True:

        user_choice = input("""
        0 - Показать все вакансии
        1 - Указать город для поиска
        2 - Отсортировать вакансии по ЗП
        3 - Вывести топ N вакансий по ЗП
        4 - Выйти
        Выберите нужный вариант: """).strip()

        if user_choice == '0':
            for item in vacancies_list:
                print(item)

            save_vacancies(vacancies_list)

        elif user_choice == '1':
            city_for_sorting = input("Введите название города: ")
            pass

        elif user_choice == '2':
            sorted_vacancies = Vacancy.sort_by_salary(vacancies_list)

            for vacancy in sorted_vacancies:
                print(vacancy)

            save_vacancies(sorted_vacancies)

        elif user_choice == '3':

            top_n = int(input("Введите количество вакансий для вывода в топ N: ").strip())

            top_n_vacancies = Vacancy.get_top_n_vacancies_by_salary(vacancies_list, top_n)

            for vacancy in top_n_vacancies:
                print(vacancy)

            save_vacancies(top_n_vacancies)

        elif user_choice == '4':
            break  # exit()

        else:
            print("Попробуйте еще раз.")
            continue
