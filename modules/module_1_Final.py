#Дополнительное практическое задание по модулю*

#input
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#to have sorted keys
students_alphabetical = list(students)
students_alphabetical.sort()
#https://docs.python.org/3/library/stdtypes.html#lists 

#output
grades_average = {students_alphabetical[ii]: sum(grades[ii]) / len(grades[ii]) for ii in range(len(grades))}
#https://docs.python.org/3/library/stdtypes.html#dict was used as an idea described by sentence "Use a dict comprehension"

print(grades_average)

