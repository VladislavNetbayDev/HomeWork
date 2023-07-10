"""
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""


a1 = int(input("input first element:"))
d = int(input("input difference of elements: "))
n = int(input("input count of elements: "))
res = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*res)