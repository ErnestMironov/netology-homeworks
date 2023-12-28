import csv


def read_csv_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def format_description(row):
    sex_map = {'female': 'женского пола', 'male': 'мужского пола'}
    sex = sex_map.get(row['sex'], 'неопределенного пола')

    age = row['age'] if row['age'] else 'неизвестного возраста'
    device = row['device_type']
    browser = row['browser']
    bill = row['bill']
    region = row['region']

    return (f"Пользователь {row['name']} {sex}, {age} лет совершил(а) покупку на {bill} у.е. "
            f"с {device} браузера {browser}. Регион, из которого совершалась покупка: {region}.")


def write_descriptions_to_file(descriptions, output_file_path):
    """ Запись списка описаний в текстовый файл. """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for description in descriptions:
            file.write(description + '\n')


def main():
    input_file_path = 'web_clients_correct.csv'
    output_file_path = 'client_descriptions.txt'

    data = read_csv_data(input_file_path)
    descriptions = [format_description(row) for row in data]
    write_descriptions_to_file(descriptions, output_file_path)


if __name__ == '__main__':
    main()
