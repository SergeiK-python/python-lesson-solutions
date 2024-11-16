# Домашнее задание по теме "Генераторы"

def all_variants(text: str):
    for j in range(1, len(text) + 1):
        for i in range(0, len(text) - j + 1):
            yield text[i:i+j]


a = all_variants("abc")
for i in a:
    print(i)