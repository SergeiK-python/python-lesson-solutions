# Домашнее задание по теме "Декораторы"

def is_prime(function):

    def is_prime_value(value: int):
        for i in range(2, value // 2 + 1):
            if value % i == 0:
                return False
        return True

    def wrapper(*args, **kwargs):
        _result = function(*args, **kwargs)
        if is_prime_value(_result):
            print("Простое")
        else:
            print("Составное")
        return _result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)