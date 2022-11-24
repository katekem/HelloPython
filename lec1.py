# print('Hello world')
# value = None
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 12333
# print(type(value))
# s = 'qwerty'
# print(s) # вывод строки
# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = [1,2,3]
# list2 = ['1','2', '3', 'qwerty']
# print(list)
# print(list2)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(f'a = {a}, b = {b}')
# print(a, b, a+b)

# a = 2
# b = 8
# c = a // b
# print(c)

# a = 3
# a += 5
# print(a)

# a = 1 < 3 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print (a==b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f)

# is_odd = f[1] % 2 == 0
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Катя':
#     print('Ура! Это КАТЯ!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# While
# original = 23
# inverted = 0 
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# For
# list = [1, 2, 3, 10, 4]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2): # начало, кол-во, приращение
#     print(i)

# for i in 'qwerty':
#     print(i)

# text = 'съешь еще этих мягких французских булок'
# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))
# for c in text:
#     print(c)

# print(text[0])            # с
# print(text[1])            # ъ
# print(text[len(text)-1])  # к  минус 1 нужен, т.к. индексация с нуля. 
#                           # Т.е. если просто указать len, то выдаст ошибку
# print(text[-5])           # б
# print(text[:])            # print(text)
# print(text[:2])           # съ - от нулевого символа до второго
# print(text[len(text)-2:]) # ок
# print(text[2:9])          # ешь еще - от второго до девятого
# print(text[6:-18])        # ешь еще этих мягких
# print(text[0:len(text):6])# сеикакл
# print(text[::6])          # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: ведение
# numbers = [1, 2, 3, 4]
# print(numbers)
# ran = range(1,6)
# numbers = list(ran)
# print(numbers)
# numbers[0] = 10
# print(numbers)
# print(len(numbers))
# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2) # redred greengreen blueblue

# colors.append('gray')  # добавить в конец списка
# print(colors == ['red', 'green', 'blue', 'gray'])   # True
# colors.remove('red')   # del colors[0]  #убрать из списка
# del colors[0]

# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))