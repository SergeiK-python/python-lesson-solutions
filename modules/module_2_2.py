#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Последнее число: "))

if first == second == third :
    print(3)
elif first == second or first == third or third == second :
    print(2)
else :
    print(0)