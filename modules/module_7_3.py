# Домашнее задание по теме "Оператор "with".

class WordsFinder:
    _escapes = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']

    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        def _remove_empty(donor: list[str]):
            recipient = []
            with_already_exists = True
            for _str in donor:
                if _str != '' and (with_already_exists or not recipient.__contains__(_str)):
                    recipient.append(_str)
            return recipient

        def _get_all_words(file_name: str) -> list[str]:
            words = []
            with open(file_name, encoding='utf-8') as file:
                content = file.read().lower()
                for escape in WordsFinder._escapes:
                    content = content.replace(escape,' ')
                words = content.split()
                words = _remove_empty(words)

            return words

        dictionary = {}
        for file_name in self.file_names:
            dictionary[file_name] = _get_all_words(file_name)

        return dictionary

    def find(self, word: str):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            result[name] = words.index(word) + 1
        return result


    def count(self, word: str):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            result[name] = words.count(word)
        return result

#test1
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#test2
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

#test3
# finder1 = WordsFinder('Rudyard Kipling - If.txt')
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

#test4
# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

#test5
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
#
# SOLUTION = {'Walt Whitman - O Captain! My Captain!.txt':
# ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman'],
# 'Rudyard Kipling - If.txt':
# ['if', 'if', 'you', 'can', 'keep', 'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 'talk', 'too', 'wise', 'if', 'you', 'can', 'dream', '—', 'and', 'not', 'make', 'dreams', 'your', 'master', 'if', 'you', 'can', 'think', '—', 'and', 'not', 'make', 'thoughts', 'your', 'aim', 'if', 'you', 'can', 'meet', 'with', 'triumph', 'and', 'disaster', 'and', 'treat', 'those', 'two', 'impostors', 'just', 'the', 'same', 'if', 'you', 'can', 'bear', 'to', 'hear', 'the', 'truth', 'you’ve', 'spoken', 'twisted', 'by', 'knaves', 'to', 'make', 'a', 'trap', 'for', 'fools', 'or', 'watch', 'the', 'things', 'you', 'gave', 'your', 'life', 'to', 'broken', 'and', 'stoop', 'and', 'build', '’em', 'up', 'with', 'worn-out', 'tools', 'if', 'you', 'can', 'make', 'one', 'heap', 'of', 'all', 'your', 'winnings', 'and', 'risk', 'it', 'on', 'one', 'turn', 'of', 'pitch-and-toss', 'and', 'lose', 'and', 'start', 'again', 'at', 'your', 'beginnings', 'and', 'never', 'breathe', 'a', 'word', 'about', 'your', 'loss', 'if', 'you', 'can', 'force', 'your', 'heart', 'and', 'nerve', 'and', 'sinew', 'to', 'serve', 'your', 'turn', 'long', 'after', 'they', 'are', 'gone', 'and', 'so', 'hold', 'on', 'when', 'there', 'is', 'nothing', 'in', 'you', 'except', 'the', 'will', 'which', 'says', 'to', 'them', '‘hold', 'on’', 'if', 'you', 'can', 'talk', 'with', 'crowds', 'and', 'keep', 'your', 'virtue', 'or', 'walk', 'with', 'kings', '—', 'nor', 'lose', 'the', 'common', 'touch', 'if', 'neither', 'foes', 'nor', 'loving', 'friends', 'can', 'hurt', 'you', 'if', 'all', 'men', 'count', 'with', 'you', 'but', 'none', 'too', 'much', 'if', 'you', 'can', 'fill', 'the', 'unforgiving', 'minute', 'with', 'sixty', 'seconds’', 'worth', 'of', 'distance', 'run', 'yours', 'is', 'the', 'earth', 'and', 'everything', 'that’s', 'in', 'it', 'and', '—', 'which', 'is', 'more', '—', 'you’ll', 'be', 'a', 'man', 'my', 'son', 'rudyard', 'kipling'],
# 'Mother Goose - Monday’s Child.txt':
# ['monday’s', 'child', 'monday’s', 'child', 'is', 'fair', 'of', 'face', 'tuesday’s', 'child', 'is', 'full', 'of', 'grace', 'wednesday’s', 'child', 'is', 'full', 'of', 'woe', 'thursday’s', 'child', 'has', 'far', 'to', 'go', 'friday’s', 'child', 'is', 'loving', 'and', 'giving', 'saturday’s', 'child', 'works', 'hard', 'for', 'a', 'living', 'and', 'the', 'child', 'that', 'is', 'born', 'on', 'the', 'sabbath', 'day', 'is', 'bonny', 'and', 'blithe', 'and', 'good', 'and', 'gay', 'mother', 'goose']}
#
# ANSWER = finder1.get_all_words()
#
# for file_name, words in SOLUTION.items():
#     _words = ANSWER.get(file_name)
#     if len(words) != len(_words):
#         print(f'the sizes are different: {len(words)} vs {len(_words)}')
#     else:
#         for ii in range(0, len(words)):
#             if words[ii] != _words[ii]:
#                 print(f'the content is different: {{{words[ii]}}} vs {{{_words[ii]}}}')
