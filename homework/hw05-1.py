'''
Напишите функцию f, которая на вход принимает два числа a и b,
и возводит число a в целую степень b с помощью рекурсии.
'''


def f(a, b):
    if b == 0:
        return 1
    else:
        return a * f(a, b - 1)


a = 3
b = 5
print(f(a, b))

# def fun(qty):
#     if qty == 0:
#         return '!'
#     number = input("Введите число: ")
#     return fun(qty - 1) + number
