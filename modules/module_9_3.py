# Домашнее задание по теме "Генераторные сборки"

def is_different_length_in_pair(pair: tuple):
    return len(pair[0]) != len(pair[1])

def is_different_on_position(index : int, _first: list, _second: list):
    if index < len(_first) and index < len(_second):
        return is_different_length_in_pair((_first[index], _second[index]))
    return True

def length_difference(pair: tuple):
    return len(pair[0]) - len(pair[1])

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (length_difference(x) for x in zip(first, second) if is_different_length_in_pair(x))
second_result = (not is_different_on_position(x, first, second) for x in range(max(len(first), len(second))))

print(list(first_result))
print(list(second_result))
