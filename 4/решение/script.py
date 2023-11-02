documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_owner_by_number(number):
    for doc in documents:
        if doc['number'] == number:
            return doc['name']
    return None


def get_shelf_by_number(number):
    for shelf, nums in directories.items():
        if number in nums:
            return shelf
    return None


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'p':
            number = input("Введите номер документа: ")
            owner = get_owner_by_number(number)
            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ не найден")
        elif command == 's':
            number = input("Введите номер документа: ")
            shelf = get_shelf_by_number(number)
            if shelf:
                print(f"Документ хранится на полке: {shelf}")
            else:
                print("Документ не найден")


if __name__ == "__main__":
    main()
