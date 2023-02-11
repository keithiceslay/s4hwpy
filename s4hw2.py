# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2  
my_list = []
old_num = num
while i <= num:
    if num % i == 0:
        my_list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old_num}: {my_list}")
