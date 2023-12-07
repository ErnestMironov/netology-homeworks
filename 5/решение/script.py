from datetime import datetime

# Форматы дат для каждой газеты
date_formats = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y"
}


def convert_date(newspaper, date_str):
    try:
        return datetime.strptime(date_str, date_formats[newspaper])
    except ValueError:
        return "Неверный формат даты"


# Цикл для обработки ввода пользователя
while True:
    user_input = input(
        "Введите название газеты и дату (или 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        break

    try:
        newspaper, date_str = user_input.split(' — ')
        converted_date = convert_date(newspaper, date_str)
        print(f"Преобразованная дата: {converted_date}")
    except (ValueError, KeyError):
        print("Неверный ввод. Попробуйте еще раз.")
