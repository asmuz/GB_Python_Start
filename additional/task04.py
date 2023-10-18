"""
Сжатие строки
Напишите программу, которая сжимает строку, заменяя повторяющиеся символы
на число и символ. Например, строка "aaabbbbcc" должна стать "3a4b2c".
"""


def compress_string(input_string):
    compressed = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed += str(count) + input_string[i - 1]
            count = 1

    compressed += str(count) + input_string[-1]
    return compressed


# Пример использования:
input_string = "aaabbbbcc"
compressed_string = compress_string(input_string)
print(compressed_string)
