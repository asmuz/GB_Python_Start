"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
"""

# var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

# Введите ваше решение ниже
# Преобразуем строки в списки чисел
set1 = set(map(int, var2.split()))
set2 = set(map(int, var3.split()))

# Находим пересечение множеств
intersection = set1.intersection(set2)

# Преобразуем пересечение в список и сортируем его
result = sorted(list(intersection))

# Выводим результат
for num in result:
    print(num, end=' ')