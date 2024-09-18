#Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ii = 0
sz = len(my_list)
while ii < sz:
    if my_list[ii] > 0:
        print(my_list[ii])
    elif my_list[ii] < 0:
        break
    ii += 1
