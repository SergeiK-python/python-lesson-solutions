# Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name: str, strings: list[str]):
    strings_positions: dict = {}
    file = open(file_name, 'w', encoding='utf-8')
    for ii in range(len(strings)):
        strings_positions[(ii + 1, file.tell())] = strings[ii]
        file.write(strings[ii] + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)