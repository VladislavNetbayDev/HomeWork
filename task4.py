"""
Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""
summ = int(input("Введите общее число журавликов: "))
Petya = int(summ/6)
Katya = int(summ/6*4)
Serezha = int(summ/6)
print(Petya, Katya, Serezha)
