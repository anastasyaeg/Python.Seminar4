#52.	Дана последовательность чисел. Получить список неповторяющихся
#  элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

#list1 = [1, 2, 3, 5, 1, 5, 3, 10]
#list2 = []

#list2.append(list1[0])
#for i in list1:
#    count = 0
#    for j in list2:
#        if i == j:
#            count +=1
#    if count == 0: list2.append(i)
           
#print(list1)
#print(list2)


# 53. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
#k = 5
#equation_str = reduce(lambda x,y:  x+y, [str(i) + '**x' + str(random.randint(0, 100)) + ' + ' for i in range(k + 1)])
#print(equation_str)
#equation_str = equation_str[-4: -len(equation_str) - 1: -1]
#equation_str += ' = 0'
#print(equation_str)
#with open('ex53.txt', 'w') as file:
#    file.write(equation_str)



#55. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

#file_numbers = 'seminar_03_02_22/file.txt'
# with open(file_numbers, 'w') as data_text:
#     data_text.writelines(input())

#with open(file_numbers) as fn:
#        data = fn.readlines()
    
#list1 = [int(i) for i in data if i != ' ']
#print(list1)

# def number(x):
#     return x-1
# for i in range(len(list1)-1, -1, -1):
#     if list1[i] - 1  != list1[i-1]:
#         print(list1[i] - 1)
#         break 

#temp_num = [list1[i] for i in range(len(list1)-1, -1, -1) \
#    if list1[i] - 1  != list1[i-1]]
#print(temp_num)
#num = lambda x: x-1
#print(num(temp_num[0]))