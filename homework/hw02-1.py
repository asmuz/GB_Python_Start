"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""
coins =  [1, 0, 1, 1, 0]
orel = 0
reshka = 0

for i in range(len(coins)):
    if coins[i] == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(orel)
else:
    print(reshka)