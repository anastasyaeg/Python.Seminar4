# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# x = True 
# y = True
# x = False
# # y = False

# def its_true(a, b):
#     f1 = not (a or b)
#     f2 = not a and not b
#     return f1 == f2
# print(its_true(x,y))

# 20. Задать номер четверти, показать диапазоны для возможных координат
# (x > 0 and y > 0): '1',
# (x < 0 and y > 0): '2',
# (x < 0 and y < 0): '3',
# (x > 0 and y < 0): '4'

# def quatro(a):
#     if a==1: return 'x > 0 and y > 0'
#     elif a==2: return 'x < 0 and y > 0'
#     elif a==3: return 'x < 0 and y < 0'
#     elif a==4: return 'x > 0 and y < 0'
#     else: 'Неверно указан номер четверти'
# a = int(input('Введите номер четверти - '))
# print(quatro(a))

# 22. Найти расстояние между точками в пространстве 2D/3D

# 24. Найти кубы чисел от 1 до N
# def find_cube(b):
#     return [n**3 for n in range(1, b)]
# b = int(input('Введите конечное число - '))
# print(find_cube(b))
    
# 26. Возведите число А в натуральную степень B используя цикл
# def get_number(a, b):
#     temp = 1
#     for n in range(b):
#         temp *= a
#     return temp

# A = int(input('введите число - '))
# B = int(input('Введите степень - '))
# print(get_number(A, B))

# 28. Подсчитать сумму цифр в числе
# def sum_in_number(n):
#     sum = 0
#     for i in n:
#         sum += int(i)
#     return sum
# n = list(input('Введите число -'))
# print(sum_in_number(n))
