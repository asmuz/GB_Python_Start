"""
Сравнение двух строк
Напишите программу, которая сравнивает две строки и сообщает,
являются ли они анаграммами (содержат одни и те же буквы в разном порядке).
"""


def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Эти строки - анаграммы.")
    else:
        print("Эти строки не анаграммы.")


string1 = "listen"
string2 = "silent"
are_anagrams(string1, string2)
