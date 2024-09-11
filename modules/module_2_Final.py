#Дополнительное практическое задание по модулю*
import random


def get_password(number):
    password = ""
    for ii in range(1, number):
        for jj in range(ii + 1, number):
            if number % (ii + jj) == 0:
                password += str(ii) + str(jj)

    return password

def print_passwords(_min, _max):
    print("all passwords:")
    for ii in range(_min, _max + 1):
        print(f"{ii} - {get_password(ii)}")

# program settings
_min = 3
_max = 20

print_passwords(_min, _max)

# a small game for winners
print("play a bit my friend")
selections = [ii for ii in range(_min, _max + 1)]
while True:
    number = random.choice(selections)
    selections.remove(number)
    password = input(f"get your number for {number}: ")
    if password == get_password(number):
        if len(selections) == 0:
            print("ok, boss, go ahead")
            break
        print("ok, but we continue")
    else:
        print("not ok, lay here for a while with others")
        break