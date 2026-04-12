'''
Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.
'''

nums = [int(_) for _ in input().split()]
res_dict = {}

for n in nums:
    res_dict[n] = res_dict.get(n, 0) + 1

res_list = [k for k, v in res_dict.items() if v > 1]

print(*sorted(res_list))
                