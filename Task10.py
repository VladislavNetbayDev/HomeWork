"""
Задача 10: На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
5 -> 1 0 1 1 0
"""
coins = int(input("input count of coins: "))
count_eagle = 0
count_tail = 0
for coin in range(coins):
    coin = int(input("input eagle(1) or tail(0)"))
    if coin == 0:
        count_eagle += 1;
    else:
        count_tail += 1;
if count_eagle < count_tail:
    print(f"flip {count_eagle} coins")
else:
    print(F"flip {count_tail} coins")