"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
"""


# решение строками
n = str(385916)

l = int(n[0]) + int(n[1]) + int(n[2])
r = int(n[3]) + int(n[4]) + int(n[5])

if l == r:
    print("yes")
else:
    print("no")


# решение числом
n = 385916

n1 = n // 10
n2 = n1 // 10
n3 = n2 // 10
n4 = n3 // 10
n5 = n4 // 10
n6 = n5 // 10

l = n % 10 + n1 % 10 + n2 % 10
r = n3 % 10 + n4 % 10 + n5 % 10

if l == r:
    print("yes")
else:
    print("no")