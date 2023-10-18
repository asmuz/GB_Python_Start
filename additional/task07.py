"""
Генерация акронима
Напишите функцию, которая принимает фразу и генерирует акроним,
используя первую букву каждого слова. Например, для фразы
"Глубокое обучение с искусственными нейронами" акронимом будет "ГОСИН".
"""


def acronym_generator(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym


input_phrase = "Глубокое обучение с искусственными нейронами"
acronym = acronym_generator(input_phrase)
print(acronym)
