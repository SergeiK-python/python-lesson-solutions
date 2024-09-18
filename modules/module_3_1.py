# Домашняя работа по уроку "Пространство имён"
from operator import contains

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search: list):
    count_calls()
    is_found = False
    for _string in list_to_search:
        if string.upper() == _string.upper():
            is_found = True
            break
    return is_found


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)