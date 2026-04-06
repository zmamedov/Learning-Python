'''
Реализуйте функцию is_valid(), которая принимает один аргумент:
    string — произвольная строка.
Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, или False в противном случае.
'''

def is_valid(string):
    if len(string) in (4, 5, 6) and string.isdigit():
        return True
    else:
        return False

print(is_valid('89abc1'))
