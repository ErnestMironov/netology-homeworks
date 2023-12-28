import re


def is_valid_car_number(number):
    pattern = r'^([АВЕКМНОРСТУХ])\d{3}([АВЕКМНОРСТУХ]{2})(\d{2,3})$'
    match = re.match(pattern, number.upper())
    if match:
        return f"Номер {match.group(1)}{match.group(2)} валиден. Регион: {match.group(3)}."
    else:
        return "Номер не валиден."


def remove_consecutive_repeats(text):
    """ Удаление всех последовательных повторов слов. """
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', text)


car_id_1 = 'А222ВС96'
car_id_2 = 'АБ22ВВ193'

print(is_valid_car_number(car_id_1))  # Номер валиден
print(is_valid_car_number(car_id_2))  # Номер не валиден

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений'
print(remove_consecutive_repeats(some_string))
