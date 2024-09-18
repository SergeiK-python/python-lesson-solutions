# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(33)
print_params(22, "two")
print_params(b=25)  # it works with warning
print_params(c=[1, 2, 3])  # it works with warning

values_list = [54.32, 'Строка', False]
print_params(*values_list)

values_dict = {"a": 12, "b": "cat", "c": ["dog", "pig"]}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
# print_params(*values_list_2, a=42)  # it does not work: TypeError: print_params() got multiple values for argument 'a'
# print_params(*values_list_2, c=42)  # it works


# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных! В таком случае,
# если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
# def a(my_list = [])) – это приводит к ошибкам!
#
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)
