# 42. Найти сумму чисел списка стоящих на нечетной позиции
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Sum_noteven_number(list1):
    summa = 0
    for i, number in enumerate(list1):
        if i %2 != 0:
            summa += number
    return summa

print(Sum_noteven_number(list1))


# 44. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list2 = [1.3, 1.8, 1.9, 1.2, 3.1]

def find_drob(list2):
    list3 = []
    for i in list2:
        list3.append(round(i%1, 2))
    return list3

def find_max(list3):
    max = list3[0]
    for i in range(len(list3)):
        if list3[i] > max: max = list3[i]
    return max
def find_min(list3):
    min = list3[0]
    for i in range(len(list3)):
        if list3[i] < min: min = list3[i]
    return min

def raznostj(list2):
    list3 = find_drob(list2)
    maxi = find_max(list3)
    mini = find_min(list3)
    return maxi - mini 

print(raznostj(list2)) 


# 46. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
def fibonacci(n):
    if n in [0, 1]: return 1
    if n >0: return fibonacci(n-1) + fibonacci(n-2)
    if n < 0: return fibonacci(n+2) - fibonacci(n+1)

def list_fibonacci(min, max):
    list_fibo = []
    for i in range(min -1, max):
        list_fibo.append(fibonacci(i))
    return list_fibo

print(list_fibonacci(-10, 10))

N = 10
def feb_print(N):
    list_1 = [0]
    feb1 = 1
    feb2 = 0
    for i in range(N):
        feb1, feb2 = feb2, feb1+feb2
        list_1.append(feb2)
        list_1.insert(0,((-1) **(i) * feb2))    
    print(list_1)

feb_print(N)



# 48. Найти корни квадратного уравнения Ax² + Bx + C = 0
# b. Используя дополнительные библиотеки
def Urovnenie(a, b, c):
    D = b**2 - 4*a*c
    print(D)

    if D < 0: return print('NO')
    elif D == 0: return print(-b /(2*a))
    else:
        x1 = (-b + (D)**0.5)/(2*a)
        print(b)
        print(a)
        print(D)
        x2 = (-b -(D)**0.5)/ (2*a)
        print(b)
        print(a)
        print(D)
        return print(x1, x2)

a = 2
b = -5
c = 2
Urovnenie(a, b, c)


# 50. Вычислить число Пи c заданной точностью d
import math

d = '0.00001'
d = int(len(d) -2)
pi = round(math.pi, d)
print(pi)

print(f'Число Пи {math.pi: .3f}')

