# Функция для взаимодействия с пользователем
def user_interaction():
    # Пользователь вводит ключевое слово
    search_query = input("Привет, я помогу тебе найти работу! :)\nВведите поисковый запрос: ")

    # Получение нужных вакансий с HH.ru

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
            pass
        elif user_choice == '1':
            city_for_sorting = input("Введите название города: ")
            pass
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            pass
        elif user_choice == '4':
            break  # exit()
        else:
            print("Попробуйте еще раз.")
            continue
