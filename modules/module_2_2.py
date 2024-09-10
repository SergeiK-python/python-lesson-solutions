#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = str(input("Первое число:"))
second = str(input("Второе число:"))
third = str(input("Последнее число:"))

if first == second == third :
    print(3)
elif first == second or first == third or third == second :
    print(2)
else :
    print(0)