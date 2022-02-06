# 31. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д

#def GetSet(N):
#        set = {1}
#    temp = 1
#    for i in range(1,N):
#        temp *= -3
#        set.add(temp)
#    return set

#print(GetSet(10))
#list = GetSet(10)
#print(list)



# 32. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1

#def GetDictionary(N):
#    dict = {}
#    for k in range(1,N+1):
#        dict[k] = 3 * k + 1
#    print(dict)

#N = int(input('Введите число N>>> '))
#GetDictionary(N)



# 36. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

#def GetSumList(n):
#    list = []
#    sum = 0
#    for i in range(1, n+1):
#        temp = (1 + 1 / i)**i
#        list.append(temp)
#        sum += temp
#        i+=1
#    print(list)
#    return sum

#print(GetSumList(7))



# 38. Реализовать алгоритм перемешивания списка

#import random 
#a = [1, 2, 3, 4, 5, 6]  
#random.shuffle(a) 
#print(a)