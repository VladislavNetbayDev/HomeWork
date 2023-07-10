"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""


list = [1, 2, -5, 7, 8, 9, -10, 3, 5]
max_number = int(input("input max_number: "))
min_number = int(input("input min_number: "))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)