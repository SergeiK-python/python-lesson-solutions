# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    """
    Функция apply_all_func принимает список целых чисел и произвольное количество функций,
    возвращает словарь результатов применения переданных функций к элементам переданного списка.
    """
    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
