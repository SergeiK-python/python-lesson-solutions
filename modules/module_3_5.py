# Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        if first == 0:  # zero on the first function call and zeros on the end of the number
            return 1
        else:
            return first  # according to task algorithm description
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


value = 40203
result = get_multiplied_digits(value)
print(f"number {value}, result {result}")
value = 4020300  # <- should this case return 0?
result = get_multiplied_digits(value)
print(f"number {value}, result {result}, <- should this case return 0?")
value = 0  # <- should this case return 0?
result = get_multiplied_digits(value)
print(f"number {value}, result {result}, <- should this case return 0?")
print("the questions are here, because this was not described in the task conditions")
