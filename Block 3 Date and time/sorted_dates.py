'''
Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.
'''

from datetime import date

n = int(input())
dates = [date.fromisoformat(input()) for d in range(n)]

for d in sorted(dates):
    print(d.strftime('%d/%m/%Y'))
    