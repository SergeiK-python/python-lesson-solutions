# Дополнительное практическое задание по модулю*

def calculate_structure_sum(arg, *args):
    added = 0
    if isinstance(arg, int):
        added = arg
    elif isinstance(arg, float):
        added = arg  # maybe this case should be ignored or not, who knows
    elif isinstance(arg, str):
        added = len(arg)
    elif isinstance(arg, list):
        for item in arg:
            added += calculate_structure_sum(item)
    elif isinstance(arg, tuple):  # to list case
        added = calculate_structure_sum(list(arg))
    elif isinstance(arg, set):  # to list case
        added = calculate_structure_sum(list(arg))
    elif isinstance(arg, dict):  # to list case
        # added += calculate_structure_sum(arg.keys(), arg.values())  # it does not work,
        # because arg.keys(), arg.values() have special types, those are not a list
        # added = calculate_structure_sum([*arg.keys(), *arg.values()])  # it is available and works
        added = calculate_structure_sum(list(arg.keys()) + list(arg.values()))

    if args is None or args == ():
        return added

    return added + calculate_structure_sum(args)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
