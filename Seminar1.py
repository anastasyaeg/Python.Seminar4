# 0. Вывести квадрат числа

# a = int(input('Введите число '))
# print (f'Квадрат числа {a} равен {a**2}')


# 1. По двум заданным числам проверять является ли первое квадратом второго

# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# print(a == b**2)


# 2. Даны два числа. Показать большее и меньшее число

# def min_max_num (a, b):
#     if a>b:
#         print(f'Максимальное число {a}, минимальное число {b}')
#     else:
#         print(f'Максимальное число {b}, минимальное число {a}')

# a = 4
# b = 7
# min_max_num (a, b)


# 3.По заданному номеру дня недели вывести его название

# week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# day_number = int(input('Введите номер дня недели '))
# print(week[(day_number-1)])


# 4. Найти максимальное из трех чисел

# def max_three (a, b, c):
#     max = a 
#     if b>max:
#         max = b
#     if c>max:
#         max = c
#     return max

# a = 700
# b = 100
# c = 23
# print(max_three (a, b, c))

# 5 Написать программу вычисления значения функции y = f(a) (sin x)

# import math

# x = int(input('Введите значение угла '))

# def sinus(x):
#     y = math.sin(math.radians(x))
#     return y
# print(sinus(x))

# 6 Выяснить является ли число чётным

# a = int(input('Введите число '))
# def number (a):
#     if a % 2 == 0:
#         print(f'Число {a} - четное')
#     else:
#         print(f'Число {a} - нечетное')
# number (a)

# Вариант с правда/ложь
# a = int(input('Введите число '))
# print(a % 2 == 0)


# 7 Показать числа от -N до N

# N = int(input('Введите число '))
# show_numbers = range(-N, N+1)
# for i in show_numbers:
#     print(i)


# 8 Показать четные числа от 1 до N

# N = int(input('Введите число '))

# def numbers (N):
#     for i in range (1, N+1):
#         if i % 2 == 0:
#             print(i)
# numbers (N)


# 9 Показать последнюю цифру трёхзначного числа

# N = int(input('Введите трехзначное число '))
# def third_num (N):
#     res = N % 10
#     return res
# print(third_num (N))


# 10 Показать вторую цифру трёхзначного числа

# N = int(input('Введите трехзначное число '))

# def second_num (N):
#     res = (N % 100) // 10
#     return res
# print (second_num (N))


# 11 Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# N = int(input('Введите число от 10 до 99: '))
# def max_num (N):    
#     first_num = N // 10
#     second_num = N % 10
#     res = max(first_num, second_num)
#     return res
# print (max_num (N))    


# 12 Удалить вторую цифру трёхзначного числа

# N = int(input('Введите трехзначное число '))

# def delete_second_num (N):
#     first = N % 10
#     third = N // 100
#     res = third*10 + first
#     return res
# print (delete_second_num (N))

# 13 Выяснить, кратно ли число заданному, если нет, вывести остаток.

# a = int(input('Введите большее число '))
# b = int(input('Введите меньшее число '))

# def number (a, b):
#     if a % b == 0:
#         res = (f'{a} кратно {b}')
#     else:
#         res = a % b
#     return res
# print (number (a, b))


# 14 Найти третью цифру числа или сообщить, что её нет

# N = int(input('Введите число '))

# def third_num (N):
#     res = (N % 100) // 10
#     return res
# print (second_num (N))


# 15 Дано число. Проверить кратно ли оно 7 и 23

# N = int(input('Введите число '))
# print (N % 7 == 0 and N % 23 == 0)