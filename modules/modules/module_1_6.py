#Практическое задание по теме: "Словари и множества"

my_dict = {"Alex": 2020, "Bob" : 2000, "Jane" : 1567}
print('Dict:', my_dict)
print('Existing value:', my_dict.get("Alex"))
#print(my_dict.get("Antony")) # also there are no errors with returned None case
print('Not existing value:', my_dict.get("Antony", "Is absent"))
my_dict.update({"Joe": 2020, "Ann" : 2000})
print('Deleted value:', my_dict.pop("Alex"))
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 3, 3, 4, "Bob", "Ann", "Bob", (12, 3.7, True)}
print('Set:', my_set)
my_set.update([7, "Joe"])
my_set.discard("Bob")
#my_set.discard((12, 3.7, 1)) # it also works (with warning message bool -> int)
print('Modified set:', my_set)