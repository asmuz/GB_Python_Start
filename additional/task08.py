"""
Реверс списка
Напишите программу, которая переворачивает список.
Не используйте встроенные функции Python для реверса.
"""


def reverse_list(input_list):
    reversed_list = input_list[::-1]
    return reversed_list


input_list = [1, 2, 3, 4, 5]
reversed = reverse_list(input_list)
print(reversed)
