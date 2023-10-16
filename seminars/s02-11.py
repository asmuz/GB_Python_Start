"""
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
оно является, то есть выведите такое число n, что φ(n)=A. Если А не является
числом Фибоначчи, выведите число -1.
"""
A = int(input("Введите натуральное число A:"))
prev = 0
curr = 1
n = 1

while curr < A:
    temp = curr
    curr += prev
    prev = temp
    n += 1

if curr == A:
    print(f"Число {A} является {n}-м числом Фибоначчи.")
else:
    print(f"Число {A} не является числом Фибоначчи")