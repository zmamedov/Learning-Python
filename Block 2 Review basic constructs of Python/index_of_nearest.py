'''
Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
        numbers — список целых чисел;
        number — целое число.
Функция должна находить в списке numbers число, ближайшее по значению к числу number, и возвращать его индекс. Если список numbers пуст, функция должна вернуть число −1.
'''

def index_of_nearest(numbers, number):
    if numbers:
        nearest_number = min(numbers, key=lambda x: abs(x - number))
        return numbers.index(nearest_number)
    else:
        return -1
        
print(index_of_nearest([7, 13, 3, 5, 18], 0))        
