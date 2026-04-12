'''
Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.
'''

def spell(*args):
    res = {}
    lowered_list = [s.lower() for s in args]
    for word in lowered_list:
        if word[0] in res:
            if len(word) > res[word[0]]:
                res[word[0]] = len(word)
        else:
            res[word[0]] = len(word)
            
    return res
                