# Самостоятельная работа по уроку "Произвольное число параметров".

def single_root_words(root_word: str, *other_words):
    same_words = []
    root_word = root_word.upper()
    for word in other_words:
        upper_word = word.upper()
        # if upper_word.__contains__(root_word) or root_word.__contains__(upper_word):
        if upper_word in root_word or root_word in upper_word:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
