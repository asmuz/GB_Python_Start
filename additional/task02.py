"""
Обратная строка
Напишите функцию, которая переворачивает строку задом наперед.
Например, строка "hello" должна превратиться в "olleh".
"""


def reverse_string(input_string):
    return input_string[::-1]


string = "Hello, world!"
print(string)
print(reverse_string(string))
