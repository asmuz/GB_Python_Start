"""
Задача №5. Решение в группах
Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать, что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6
"""

a = int(input("В какой вагон сел? "))
b = int(input("Какой номер по порядку? "))
if a == b:
    print("Невозможно посчитать количество вагонов")
else:
    print("Всего ", a + b - 1," вагонов")