"""
Подсчет символов
Напишите программу, которая принимает строку от пользователя и подсчитывает,
сколько раз каждый символ встречается в этой строке.
"""


def count_characters(input_string):
    character_count = {}
    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


input_string = "Hello, World!"
result = count_characters(input_string)
print(result)
