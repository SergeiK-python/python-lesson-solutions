#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = ([1,2,3], True, "Cat")
print(immutable_var)
#immutable_var[1] = False
mutable_var = [[1,2,3], True, "Cat"]
mutable_var[2] = "Dog"
print(mutable_var)