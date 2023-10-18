"""
Палиндромные подстроки
Напишите программу, которая находит все палиндромные подстрокив заданной строке.
Например, для строки "ababa" программа должна выдать ["aba", "bab"].
"""


def find_palindromes(input_string):
    palindromes = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1] and len(substring) > 1:
                palindromes.append(substring)
    return palindromes


input_string = "ababa"
palindrome_list = find_palindromes(input_string)
print(palindrome_list)
