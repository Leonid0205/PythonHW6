# 0 - Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок,
# меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

# def check_digit(str1):
#     for i in str1:
#         if i.isalpha():
#             return True
# def create_list_of_digits(str1):
#     list_of_digits = []
#     str1 = str1 + ' '
#     str_digits = ''
#     for i in str1:
#         if i.isdigit():
#             str_digits += i
#         else:
#             list_of_digits.append(str_digits)
#             str_digits = ''
#     if str1[0] == '-':
#         list_of_digits[1] = str1[0] + list_of_digits[1]
#     list_of_digits = list(filter(lambda x: x != '', list_of_digits))
#     list_of_digits = list(map(float, list_of_digits))
#     return list_of_digits
# def create_znak_of_list(str1):
#     if str1[0] == '-':
#         str1 = str1[1::]
#     list_of_znak = list(filter(lambda x: x == '/' or x == '*' or x == '-' or x == '+', str1))   
#     return list_of_znak
# def shorten_list(i ,list1, list2):
#     del list1[i + 1]
#     del list2[i]
#     return list1, list2
# def calculate(list_of_digits, list_of_znak):
#     while len(list_of_znak) > 0:
#         while '/' in list_of_znak:
#             for e, i in enumerate(list_of_znak):
#                 if i == '/':
#                     list_of_digits[e] = list_of_digits[e] / list_of_digits[e + 1]
#                     shorten_list(e, list_of_digits, list_of_znak)
#         while '*' in list_of_znak:
#             for e, i in enumerate(list_of_znak):
#                 if i == '*':
#                     list_of_digits[e] = list_of_digits[e] * list_of_digits[e + 1]
#                     shorten_list(e, list_of_digits, list_of_znak)
#         while '-' in list_of_znak:
#             for e, i in enumerate(list_of_znak):
#                 if i == '-':
#                     list_of_digits[e] = list_of_digits[e] - list_of_digits[e + 1]
#                     shorten_list(e, list_of_digits, list_of_znak)
#         while '+' in list_of_znak:
#             for e, i in enumerate(list_of_znak):
#                 if i == '+':
#                     list_of_digits[e] = list_of_digits[e] + list_of_digits[e + 1]
#                     shorten_list(e, list_of_digits, list_of_znak)
#     return list_of_digits[0]
# while True:
#     try:
#         str1 = input('Input an expression for calculating: ')
#         str1 = str1.replace(' ','')
#         if check_digit(str1):
#             print('Invalid input!')
#         else:
#             list_of_digits = create_list_of_digits(str1)
#             list_of_znak = create_znak_of_list(str1)
#             print(f'{str1} = {calculate(list_of_digits, list_of_znak)}')
#             break
#     except:
#         print('Not enough digits')



# 1 - Определить, присутствует ли в заданном списке строк, некоторое число
# ['asdasd', 'dasd', 'asdfghh1', 'AAdsadaf']

# list1 = ['asdasd', 'dasd', 'asdfghh1', '78dfsdf', 'AAdsadaf']
# n = '1'
# result1 = [list1[i] for i in range(len(list1)) for j in range(len(list1[i])) if n in list1[i][j]]
# print(result1)
# result11 = [print(True) for i in range(len(list1)) for j in range(len(list1[i])) if n in list1[i][j]]
# print(result11)

# 2 - Найти сумму чисел списка стоящих на нечетной позиции

# ist2 = [2,11,34,21,6,8,7,1]
# s_digit = sum(list2[i] for i in range(len(list2)) if i % 2 != 0)
# print(list2)
# print(s_digit)

# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# from math import sqrt

# x1, y1 = map(int, input('Input X1 coordinate and Y1 coordinate: ').split())
# print(f'X1 coordinate is {x1}, Y1 coordinate is {y1}')
# x2, y2 = map(int, input('Input X1 coordinate and Y1 coordinate: ').split())
# print(f'X2 coordinate is {x2}, Y2 coordinate is {y2}')
# distance = round((sqrt((x2- x1)**2 + (y2 -y1)**2)),3)
# print(f'Distance between X and Y is: {distance}')

# 4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# list4 = ["wqer", "asd", "qwe", "qwe", "ertqwe"]
# print(list4)
# find_str = 'qwe'
# t2 = list(filter((lambda s: s==find_str), list4))
# if len(t2) < 1:
#     print('-1')
# else:
#     print(f'Index of "{find_str}" = {list4.index(find_str)}')

# if find_str in list4:
#     x1 = [i for i, e in enumerate(list4) if e == find_str]
#     print(x1[0])
# else:   print(-1)

# 5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import math

# list5 = [2, 3, 4, 5, 6]
# list51 = list(reversed(list5))
# list5 = [list5[i] * list51[i] for i in range(math.ceil(len(list5)//2))]
# print(list5)

# 6 - Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# n = 5
# list6 = [(-3)**i for i in range(n)]
# print(list6)