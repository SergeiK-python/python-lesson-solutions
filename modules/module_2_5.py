#Домашняя работа по уроку "Функции в Python.Функция с параметром"

# here
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# list constructor "Using a list comprehension" was gotten as an idea
def get_matrix_modified(rows, columns, value):
    return [[value for ii in range(0, columns)] for jj in range(0, rows)]

# according to task request
def get_matrix(rows, columns, value):
    matrix = []
    for jj in range(0, rows):
        matrix.append([])
        for ii in range(0, columns):
            matrix[jj].append(value)
    return matrix

print("\nmodified method")
result1 = get_matrix_modified(2, 2, 10)
result2 = get_matrix_modified(3, 5, 42)
result3 = get_matrix_modified(4, 2, 13)
print(result1)
print(result2)
print(result3)

print("\nrequested method")
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
