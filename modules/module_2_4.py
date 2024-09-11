#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
from typing import no_type_check

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for value in numbers:
    if value == 1:
        continue

    is_prime = True
    #for number in primes: # <- we can face a problem in case of 'numbers' would not be a sorted solid interval
    for number in range(2, value):
        if value % number == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(value)
    else:
        not_primes.append(value)

print("Primes:", primes)
print("Not Primes:", not_primes)
