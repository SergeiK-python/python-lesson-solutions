# This is a sample Python script.
from itertools import filterfalse
from xmlrpc.client import boolean


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # some experiments
    is_: bool = True
    print(type(is_))

    x: int = 1
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
    print('0.1234567890123456789', 0.1234567890123456789)
    print('Hi \'Zerg\'') # str
    print("Hi" + 'Zerg') # "" = ''
    y : bool = True      # boolean
    print('type(y) is int:', type(y) is int)    # !!!
    print('instance is int:', isinstance(y, int)) # !!!
    print('type(y) is bool:', type(y) is bool)
    print('instance is bool:', isinstance(y, bool)) # !!!
    c = 1 + 2.0j #complex
    print(c * c.conjugate())
    print((not y) or (x < 5 < 10 * x))
    print(int('037'))
    print(bool(''))

    print("M""M")
    print("M" + "M")
    print("M" * 2)
    print("M\n" * 2)
    print("""N
N
N""") # vfc

    name : str = "Denis"
    print(name[0:3])
    print(name[::2])
    print(name[0:3:2])
    print(name[3:100])
    print(name[-1:-100:-1])
    print(name[::-1])
    print(name[-1:-100:-2])

    ii = 1
    jj = 1
    print("ii=",ii,", jj=",jj)
    print("ii=" + str(ii) + ", jj=" + str(jj))
    print(f"ii={ii}, jj={jj}")

    z : int = 1
    z = "cat"  # <- warning
    print(z, type(z))

    w = 1
    w = "cat"
    print(w, type(w))
    print(w.__str__())
    print(repr(w))
    print(w.__repr__())
    print(f"{w}")
    print(f"{w!r}")

    # https://habr.com/ru/companies/ruvds/articles/500296/
    another_name = "Denis"
    print(name == another_name)
    print(name is another_name)  # ??? True... memory optimization? str as primitive type?
    print(id(name) == id(another_name))  # ??? True... memory optimization?
    print(id(name) is id(another_name))

    tuple_ = tuple([[1,2],True,"Dog"])
    print(tuple_)
    tuple_[0].append(True)
    print(tuple_)
    tuple_[0].extend([7,6,7])
    print(tuple_)
    tuple_[0].extend((7, True, "Cat"))
    value = (7, True, "Pig")
    tuple_[0].extend(value) # added as a list
    print("\t",tuple_)
    # tuple_.pop(0) # error
    tuple_[0].remove(True) # it does not work! It deletes the first element
    print(tuple_)
    tuple_[0].remove(7)  # it works well (deletes the first occurrence of 7)
    print(tuple_)
    # tuple_[0].remove(["Dog"]) # fall down, it is not presented
    tuple_[0].remove("Pig") # done well
    print(tuple_)

    tuple_ = tuple({5, 6, 7})
    print(tuple_)


def lists_() -> str:
    print("---lists tests---")
    list_ = ["0", "1", "2", "2", "3"]
    print(list_)
    list_.pop(1) # Remove element by its index
    print(list_)
    list_[-1] = "0"
    print(list_)
    list_.remove("0") # Remove first occurrence of value!
    print(list_)

    print("---other lists tests---")
    inner = [1, 2, 3]
    array = [inner, 1, True, 0, "Cat", False]
    print(array,"      <- initial array")
    array.remove(True)
    print(array,"      <- array.remove(True) result")
    inner.append(4)
    # inner.add(5) # error
    inner.append(f"\"inner\":\"{inner}\"")
    array.remove(False)
    print(array,"      <- array.remove(False) result")
    array.remove(inner)
    print(array, "      <- array.remove(inner) result")

    print(1 == True)
    print(int(1) == True)
    print(True == 2)
    print(True == bool(2))
    print(True == boolean(2))

    list_ = list('hello')
    print(list_)
    print("".join(list_))

    list_ = [1, 3+6.6j, 8]
    print(list_)
    sum_ = sum(list_)
    print(sum_/len(list_))

    numbers = [1, 2, 3]
    for number in numbers:
        print(number, (id(number) - id(numbers[0])) // int.__sizeof__(numbers[0]), end=" ")

    return "lists tests done"


def maps_() -> str :
    print("---maps tests---")
    # map_ = {"1" : 1, "1" : 2,"3" : 3} # error
    map_ = {"1": 1, "4": 4, "3": 3}
    print(map_)
    # print(map_["5"]) # error
    print(map_.get("5")) # None
    print(map_.get("5", -1))  # -1
    print(map_)
    # del map_["5"] # error
    map_.pop("1")
    map_.update({"3": 6, "4": 8})
    print(map_)
    print(map_.keys())
    print(map_.values())
    print(map_.items())

    map_ = {(1, True, 2.0) : 1, (1, 1, 2.0) : 777, (-1, False, -2.0) : 2} # be careful =)
    print(map_)

    print(dict([[1,2], [3,4]]))  # some warning ?
    print(dict([(3, 26), (4, 44)]))  # no warnings !

    return "maps tests done"


def sets_() -> str :
    print("---sets tests---")
    set_ = {1,2,3,3,True,True}
    print(set_)
    set_.remove(True)
    print(set_)
    # set_.remove(False) # error 0 is absent
    b = set_.discard(False)
    print(set_, "removed", b)
    a = set_.pop() # removed the first element
    print(set_, "removed", a)
    set_.update([0, 2, 7, 8]) # add all
    set_.add(10) # add one
    # set_.add([9, 10]) # error not hashable object ?
    print(set_)
    # set_.pop(3) #error
    set__ = {0, 2}
    print(set__, "is subset of set", set_, "result", set__.issubset(set_))
    list_ = ["0", "1", "2", "2", "3"]
    print(set(list_))

    set_1 = {0,1}
    set_2 = {1, 2}
    print(set.intersection(set_1,set_2))
    print(set.union(set_1, set_2))
    print(set.symmetric_difference(set_1, set_2))
    return "sets tests done"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('\n', lists_(), '\n\n')
    print('\n', maps_(), '\n\n')
    print('\n', sets_(), '\n\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
