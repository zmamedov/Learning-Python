'''
Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и выводит все переданные аргументы, указывая тип каждого. Пары аргумент — тип должны выводиться каждая на отдельной строке.
'''

def print_given(*args, **kwargs):
    for el in args:
        print(el, type(el))
        
    for el in sorted(kwargs):
        print(el, kwargs[el], type(kwargs[el]))
        
print_given(1, [1, 2, 3], 'three', two=2)
