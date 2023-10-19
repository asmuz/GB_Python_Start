"""
Задача No17
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
"""
lst = [1, 1, 2, 0, -1, 3, 4, 4]

unique = []
for item in lst:
    if item not in unique:
        unique.append(item)

print(len(unique))
