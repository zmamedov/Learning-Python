'''
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.
'''

from datetime import date

date_1 = date.fromisoformat(input())
date_2 = date.fromisoformat(input())

print(min(date_1, date_2).strftime('%d-%m (%Y)'))
