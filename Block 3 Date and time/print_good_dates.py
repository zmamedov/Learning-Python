'''
Реализуйте функцию print_good_dates(), которая принимает один аргумент:
        * dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, в формате  month_name DD, YYYY, где month_name — полное название месяца на английском.
'''

from datetime import date

def print_good_dates(dates):
    interesting_dates = []
    for d in sorted(dates):
        if d.year == 1992 and (d.month + d.day) == 29:
            interesting_dates.append(d.strftime('%B %d, %Y'))
    
    if interesting_dates:
        print(*interesting_dates, sep='\n')
        