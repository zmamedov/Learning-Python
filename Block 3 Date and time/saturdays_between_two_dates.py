'''
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
    * start — начальная дата, тип date;
    * end — конечная дата, тип date.
Функция должна возвращать количество суббот между датами start и end включительно.
'''

from datetime import date

def saturdays_between_two_dates(start, end):
    date_1 = date.toordinal(min([start, end]))
    date_2 = date.toordinal(max([start, end]))
    count_sat = 0
    
    for d in range(date_1, date_2 + 1):
        if date.fromordinal(d).weekday() == 5:
            count_sat +=1
            
    return count_sat
    