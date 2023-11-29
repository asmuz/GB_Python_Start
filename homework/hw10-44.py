'''
Урок 10. Построение графиков
Задача 44: В ячейке ниже представлен код генерирующий DataFrame,которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
'''
import random
# Импортируется модуль random для генерации случайных чисел
import pandas as pd
# Импортируется модуль pandas и задается псевдоним pd

lst = ['robot'] * 10
# Создается список lst, содержащий 10 элементов со значением 'robot'
lst += ['human'] * 10
# К списку lst добавляется список, содержащий 10 элементов со значением 'human'
random.shuffle(lst)
# Список lst перемешивается
data = pd.DataFrame({'whoAmI': lst})
# Создается DataFrame с одной колонкой 'whoAmI', содержащей значения из списка lst
print(data)
# Выводим сгенерированный DataFrame

new_data = pd.DataFrame()
# Создаем новый пустой DataFrame

unique_values = data['whoAmI'].unique()
# Получаем уникальные значения из столбца 'whoAmI'

for value in unique_values:

    new_data[value] = (data['whoAmI'] == value).astype(int)
    # Для каждого уникального значения создаем новый столбец и заполняем его значениями 0 или 1

print(new_data)
# Выводим новый DataFrame в виде One Hot
