"""
Сортировка слов в строке
Напишите программу, которая принимает строку,
разбивает её на слова и сортирует слова в алфавитном порядке.
"""


def sort_words_in_string(input_string):
    input_string = input_string.lower()     # переводим строку к нижнему регистру
    # разделяем строку на отдельные слова и добавляем в список
    words = input_string.split()
    sorted_words = sorted(words)            # сортируем слова
    return ' '.join(sorted_words)           # возвращаем строку


input_string = "Python is a versatile programming language"
sorted_string = sort_words_in_string(input_string)
print(sorted_string)
