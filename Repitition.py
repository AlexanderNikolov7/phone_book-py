# Задача 1. Вывести Квадрат числа.

# n = int(input('n = '))
# print(f'квадрат числа {n} = {n**2}')

# Задача 2. Даны два числа. Показать большее и меньшее число.

# def max(a, b):
#     if a > b:
#         print(f'число {a} больше чем число {b}')
#     elif b > a:
#         print(f'число {b} больше чем число {a}')
#     else:
#         print('Эти числа равны')

# max(input('a = '), input('b = '))

# Задача 3. Найти максимальное из трёх чисел.

# list = [3, 1, 9]
# max = list[0]
# count = 1
# while count != len(list):
#     if max < list[count]:
#         max = list[count]
#     count += 1
# print(f'максимальгое число из {list} = {max}')

# for i in range(1, len(list)):
#     if list[i] > max:
#         max = list[i]
# print(f'максимальгое число из {list} = {max}')

# for i in list:
#     if i > max:
#         max = i
# print(f'максимальгое число из {list} = {max}')

# Задача 4. Является ли число чётным.
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in list:
#     if i % 2 == 0:
#         print(f'число {i} является чётным')

# num = int(input('num = '))
# if num % 2 == 0:
#     print(f'число {num} является чётным')
# else:
#     print(f'число {num} не является чётным')

# Задача 5. Показать чётные числоа от 1 до N.

# N = int(input('N = '))
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         print(i)

# ДЗ
# 1. По двум заданным числам проверять является ли первое квадратом второго.

# a = int(input('a = '))
# b = int(input('b = '))
# if a == b**2:
#     print(f'число {a} является квадратом числа {b}')
# else:
#     print(f'число {a} не является квадратом числа {b}')

# 2. По заданному номеру дня недели вывести его название.

# n = int(input("Введите день недели: "))
# if n == 1:
#     print('Это понедельник')
# elif n == 2:
#     print('Это вторник')
# elif n == 3:
#     print('Это среда')
# elif n == 4:
#     print('Это четверг')
# elif n == 5:
#     print('Это пятница')
# elif n == 6:
#     print('Это суббота')
# elif n == 7:
#     print('Это воскресенье')
# else:
#     print('Нет такого дня недели!')

# 3. Показать числа от -N до N.

# N = int(input('N = '))
# for i in range(N*-1, N + 1):
#     print(i)

# 4. Показать последнюю цифру трёхзначного числа.

# num = input('Введите трёхзначное число: ')
# print(num[2])

# 5. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа.

# a = int(input('Введите двухзначное число: '))
# b = a % 10
# c = a // 10
# if a < 100 and a >=10:
#     if b >= c:
#         print(b)
#     else:
#         print(c)
# else:
#     print('Это не двухззначное число!')

# 6. Выяснить, кратно ли число заданному, если нет, вывести остаток.

# a = 100
# b = int(input('Введите число: '))
# if a % b == 0:
#     print(f'Число {a} кратно числу {b}')
# else:
#     print(f'Число {a} не кратно числу {b} и остаток равен {a % b}')

# Задача 6. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# Задача 7. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0.

# x = int(input('x = '))
# y = int(input('y = '))

# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# else:
#     print('4 четверть')

# Задача 8. Дано число обозначающее день недели. Выяснить является номер дня недели выходным.

# num = int(input('Введите день недели: '))
# if num > 7 and num < 0:
#     print('Нет такого дня недели!')
# elif num <= 7 and num > 5:
#     print('да')
# else:
#     print('нет')

# Задача 9. Дано число. Проверить кратно ли оно 7 и 23.

# num = int(input('-->'))
# if num % 7 == 0 and num % 23 == 0:
#     print('да')
# else:
#     print('нет')

# Задача 10. Найти третью цифру числа или сообщить, что её нет.

# from random import randint
# num = str(randint(1, 999))
# if len(num) < 3:
#     print('В числе {num} нет третьей цифры')
# else:
#     print(f'В числе {num} третья цифра = {num[2]}')

# Задача 11. Программа проверяет пятизначное число на палиндромом.

# from random import randint
# num = str(randint(10000, 99999))
# if num[0] == num[-1] and num[1] == num[-2]:
#     print(f'число {num} является палиндромом')
# else:
#     print(f'число {num} не является палиндромом')

# num = input('-->')
# revers_num = ''
# for i in reversed(num):  # reversed - отсчитывает от последнего к первому индексу
#     revers_num += i

# if num == revers_num:
#     print('да')
# else:
#     print('нет')

# num = input('-->')
# if num == num[::-1]: # срезы с шагом -1 выдаёт строку задом на перёд
#     print('да')
# else:
#     print('нет')

# Задача 12. Сфрмировать список из N членов последовательности. Список записать в файл "number_lis.txt" (в одну строку одно число)
# N = 5
# with open('number_lis.txt', 'w') as data:
#     for i in range(1, N + 1):
#         data.write(f'line{i} = {i**2}\n')

# path = 'number_lis.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# Задача 13. Пользователь задаёт две строки. Определить кол-во вхождения одной строки в другой.

# st1 = 'qwertqwrtq'
# st2 = 'qw'

# flag = True
# count = 0

# while flag:
#     index = st1.find(st2)
#     if index != -1:
#         st1 = st1[index + len(st2):]
#         count += 1
#     else:
#         print(count)
#         flag = False

# Задача 14. Подсчитать сумму цифр в вещественном числе.

# num = input('Введите вещественное число: ')
# my_num = ''

# for i in range(len(num)):
#     if num[i] != '.':
#         my_num += num[i]


# new_num = int(my_num)
# sum = 0
# while new_num != 0:
#     sum = sum + new_num % 10
#     new_num = new_num // 10
# print(sum)

# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# Задача 15. Для натурального n создать словарь индекс - значение, состоящий из элементов последовательности зn + 1.

# n = 5
# res = 1
# dict = {}
# for i in range(n):
#     res = i * 3 + 1
#     dict[i] = res
# print(dict)

# Задача 16. Определить, поозицию второго вхождения строки в списке либо сообщить, что её нет.

# list = ['3', '2', '1', '4', '5', '3', '7', '3']
# st = '3'
# count = 0
# for i in range(len(list)):
#     if list[i] == st:
#         count += 1
#     if count == 2:
#         print(i + 1)
#         break
# if count < 2:
#     print('её нет')

# Задача 17. Найта сумму чисел списка стоящих на нечётной позиции.

# list = list(range(9))
# print(list)
# print(sum(list[1::2]))

# Задача 18. Найти произведение пар чисел в списке, парой считаем первый и последний элемент и т.д.

# import math

# my_list = [4, 5, 8, 1, 7, 3, 1]
# new_list = []
# index = 1
# for i in range(math.ceil(len(my_list)/2)):  # math.ceil округлет в большудю сторону
#     new_list.append(my_list[i] * my_list[-index])
#     index += 1
# print(new_list)

# Задача 19. Фибоначчи (реализовать с отрицательными цифрами)

# def Fib_rec(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fib_rec(n - 1) + Fib_rec(n - 2)   # решение для положительных чисел

# for i in range(1, 40):
#     print(Fib_rec(i))

# def Fib_rec(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fib_rec(n - 2) - Fib_rec(n - 1)   # решение для отрицательных чисел

# my_list = []
# for i in range(1, 10):
#     my_list.append(Fib_rec(i))
# print(my_list)

# Задача 20. Строка содержит набор чисел, указать большее и меньшее число.

# st = '24 6 896 46 34 63 2 5 19 3'
# st = st.split(' ')
# print(st)
# my_list = []
# for i in st:
#     my_list.append(int(i))
# print(my_list)

# Max = my_list[0]
# for i in my_list:
#     if i > Max:
#         Max = i
# print(f'наибольшее число = {Max}') # = max(my_list)
# print(max(my_list))

# Min = my_list[0]
# for i in my_list:
#     if i < Min:
#         Min = i
# print(f'наименьшее число = {Min}') # = min(my_list)
# print(min(my_list))

# Задача 21. Задать список из n чисел последовательности (1+1*n)^n и вывести на экран их сумму.

# n = 5
# my_list = []
# for i in range(n):
#     my_list.append(int((1 + 1 * i) ** i))
# print(sum(my_list))

# lis = [(1 + 1 * i) ** i for i in range(n)] # включение
# print(sum(lis))

# func = lambda x: (1 + 1 * x) ** x # lambda  def func(x):
# li = [func(i) for i in range(n)]  #            return (1 + 1 * x) ** x
# print(sum(li))

# def f(x):
#     return (1 + 1 * x) ** x
# l = list(map(f(n), [x for x in range(n)]))
# print(l)


# Задача 22. Найти сумму чисел списка стоящих на нечётной позиции.

# n = 5
# my_list = [x for x in range(n)]
# print(my_list)

# summ = 0
# for i in my_list:
#     if i % 2:
#         summ += my_list[i]
# print(summ)

# lis = list(filter(lambda x: x % 2, [x for x in range(n)]))  # filter
# print(lis)
# print(sum(lis))

# print([x for i, x in enumerate(my_list) if not i % 2])  # enumirate


# Задача 23. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.

# my_list = [4, 5, 3, 5, 6, 2, 7, 4, 5, 7, 35, 4, 3]
# print(set(my_list))

# new_list = []

# def f(x):
#     global new_list
#     if x not in new_list:
#         new_list.append(x)

# for i in my_list:
#     f(i)
# print(new_list)
# res = list(map(f, my_list))
# print(f'map--> {new_list}')

# fun = lambda x: new_list.append(x) if x not in  new_list else False
# res = list(map(fun, my_list))
# print(f'map2--> {new_list}')

# result = list(filter(lambda x: new_list.append(x) if x not in  new_list else False, my_list))
# print(f'map3--> {new_list}')

# Итоги симинара:
# List Comprehension (включения) [x for x in range(10)], [random.randint(1,10) for x in range(10)], [x for x in my_list if x != 3]
# lambda - краткая реализация функций
# map - применить функцию к набору элементов
# filter - отфильтровать
# zip - поэлементно комбинирует в кортежи

# Задача 24. Найти сумму квадратов чётных чисел на промежутке от 1 до n. Пример: n=5: [1, 2, 3, 4 ,5] --> 2^2 + 4^2 = 20

# n = 11
# my_list = list(filter(lambda x: not x % 2, [i ** 2 for i in range(n)]))
# print(my_list)
# print(sum(my_list))

# Задача 25. Из списка строк получить список, содержащий только те элементы, которые являются числами. Пример: lst = ['asd', '123', '457', 'ht', 'fwef322f'] --> ['123', '457']

# lst = ['asd', '123', '457', 'ht', 'fwef322f']
# my_list = list(filter(lambda x: x.isdigit(), lst ))
# print(my_list)

# Задача 26. Из старого списка чисел получить список элементов больше трёх.

# my_list = [4, 6, 234, 4, 8, 324, 2, 5, 1, 64, 3, 21, 4, 1]

# new_list = list(filter(lambda x: x > 3, my_list))

# res = [i for i in my_list if i > 3]

# print(new_list)
# print(res)

# Задача 27. Получить из списка чисел квадраты этих чисел.

# my_list = [2, 1, 4, 3, 6, 4, 7]

# res = list(map(lambda x: x ** 2, my_list))
# print(res)
# print(list(zip(my_list, res))) # просто используем зип для наглядности

# Задача 28. посчитайте сколько раз символ "f" встречается в строке 'foiuwerhbf34dsfkjlf'

# text = 'foiuwerhbf34dsfkjlf'

# res = list(filter(lambda i: i == 'f', text))
# print(len(res))

# Задача 29. Даны двва списка чисел, вернуть список который состоит из элементов, общих для этих двух списков.

# a = [2, 5, 4, 7, 3, 2, 5]
# b = [5, 3, 7, 5, 8, 3, 2]

# c = set(filter(lambda i: i in b, a))
# print(list(c))
# d = set([i for i in b if i in a])
# print(list(d))

# Задача 30. Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречается число 237.

# a = [34, 46, 2, 23, 7567, 235, 37, 23, 237, 84, 24, 6]
# n = [i for i in range(len(a)) if a[i] == 237]
# if n != []:
#     a = a[:n[0]]

# print([x for x in a if not x % 2])

# res = [i for i in a if not i % 2]
# print(res)

