"""
Требуется найти в массиве list_1 самый близкий
по величине элемент к заданному числу k и вывести его.
"""
# list_1 = [1, 2, 3, 4, 5]
# k = 6

# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

dif = 0
min_dif = max(list_1)
number = 0

for i in list_1:
    # dif = k - i
    dif = abs(i - k)
    if dif <= min_dif:
        min_dif = dif
        number = i

print(number)
