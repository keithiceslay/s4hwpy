# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
print('Введите степень ')
k = int(input())
my_list = []
for i in range(k+1):
    my_list.append(random.randint(0,100))
my_list.reverse()
for i in range(k+1):
    if my_list[i] != 0 and k-i != 0:
        print(f'{my_list[i]}*x^{k-i} + ', end = "")
    elif k-i == 0: print(f'{my_list[i]} == 0')
