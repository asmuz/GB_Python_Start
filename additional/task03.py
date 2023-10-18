"""
Поиск уникальных элементов
Напишите функцию, которая принимает список и возвращает новый список,
содержащий только уникальные элементы из исходного списка.
"""


def unique_elements(input_list):
    unique = []
    for item in input_list:
        if item not in unique:
            unique.append(item)
    return unique


list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(list)
print(result)
