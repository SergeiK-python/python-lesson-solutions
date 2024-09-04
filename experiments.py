# This is a sample Python script.
from itertools import filterfalse


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # some experiments
    x : int = 1
    print(type(x))
    print(type(0xA5))   # hex
    print(type(0o11))   # octo
    print(0o12)         # octo
    print(0xA)          # hex
    print(type(5 / 5))  # float
    print(type(5 // 5)) # integer
    print(type(5 % 5))  # int
    print(5 ** 2)
    print(type(5 + 2.5))
    print(2 ** 256)
    print(2.00000000001 ** 256.000000001)
    print(0xA // 2.0)   # float
    print('Hi \'Zerg\'') # str
    print("Hi" + 'Zerg') # "" = ''
    y : bool = True      # boolean
    print(y, not y)      # ~x ??? == != and or not
    print (type(y))
    print((not y) or (x < 5 < 10 * x))
    print(int('037'))
    print(bool(''))

    print("M""M")
    print("M" + "M")
    print("M" * 2)

    name : str = "Denis"
    print(name[0:3])
    print(name[::2])
    print(name[0:3:2])
    print(name[3:100])
    print(name[-1:-100:-1])
    print(name[::-1])
    print(name[-1:-100:-2])

    #https://habr.com/ru/companies/ruvds/articles/500296/
    another_name = "Denis"
    print(name == another_name)
    print(name is another_name) #??? True... memory optimization? str as primitive type?
    print(id(name) == id(another_name)) #??? True... memory optimization?
    print(id(name) is id(another_name))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
