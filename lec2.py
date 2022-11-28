# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# 	print(line)
# data.close()
# exit()

# import lec1
# print(lec1.f(1))

# def new_string(symbol, count):
# 	return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!'))   # TypeError missing 1 required...

# def new_string(symbol, count = 3):
# 	return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!'))    # !!!
# print(new_string(4))      # 12


# def concatenatio(*params):    # * вначале означает сколько угодно аргументов
# 	res: str = ""   # явно задан тип, но это необязательно
# 	for item in params:
# 		res += item
# 	return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))  # a1
# print(concatenatio(1, 2, 3, 4))  # TypeError: ...


# def fib(n):
# 	if n in [1, 2]:
# 		return 1
# 	else:
# 		return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
# 	list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34

## Кортежи
# t = ()
# print(type(t))   # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple
# colors = ['red', 'blue', 'green']
# print(colors)   # ['red', 'blue', 'green']
# t = tuple(colors)
# print(t)        # ('red', 'blue', 'green')

# a, b = 3, 4
# a = (3, 4)
# print(a)
# print(a[0])
# print(a[-1])
# a[0] = 12   # TypeError - в списках можно менять, в кортеже - нет
# for item in a:
#     print(item)


# t = tuple(['red', 'green', 'blue'])
# print(t[0])   # red
# print(t[2])   # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2])  # green
# # print(t[-200]) # IndexError: tuple index out of range

# for e in t:
# 	print(e)    # red green blue   # построчный вывод


## Распаковка кортежей
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

## Словари
dictionary = {}
dictionary = \
	{
		'up': 'стрелка вверх',
		'left': 'стрелка влево',
		'down': 'стрелка вниз',
		'right': 'стрелка вправо'
	}
# print(dictionary)    # 'up': 'стрелка вверх', 'left': 'стрелка влево', ...
# 					# 'down': 'стрелка вниз''right': 'стрелка вправо'
# print(dictionary['left'])  # стрелка влево
#  типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# del dictionary['left']  # удаление элемента

# for item in dictionary:    # for (k, v) in dictionary.items():
# 	print('{}: {}'.format(item, dictionary[item]))


## Множества
# colors = {'red', 'green', 'blue'}
# print(type(colors))  # set

# colors.add('red')
# print(colors)     # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)     # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors)     # {'green', 'blue', 'gray'}
# colors.discard('red')  # ok
# print(colors)     # {'green', 'blue', 'gray'}
# colors.clear()    # { }
# print(colors)     # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 3, 5, 8, 13, 21}
# c = a.copy()     # c = {1, 2, 3, 5, 8}
# u = a.union(b)   # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = 2, 5, 8}
# dl = a.difference(b)  # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}

# q = a \
# 	.union(b) \
# 	.difference(a.intersection(b))
# {1, 21, 3, 13}

# s = frozenset(a)


## Списки - продолжение
# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
# 	print(e)

# print()

# for e in list2:
# 	print(e)

# list1[0] = 123

## значения поменяются и во втором списке
# print()
# for e in list1:
# 	print(e)

# print()

# for e in list2:
# 	print(e)

## если поменять значения во втором списке? то поменяются значения и в первом
# list2[2] = 333
# print()
# for e in list1:
# 	print(e)

# print()

# for e in list2:
# 	print(e)


# Удаление последнего элемента из списка
list1 = [1, 2, 3, 4, 5]
print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop(2)) # удаление второго элемента по индексу, т.е. 3
# print(list1)

# Добавление нового элемента в список (не в конец)
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# print(list1.insert(2, 11))  # сначала индекс - куда, затем - значение
# print(list1)

# Добавление нового элемента в список в конец
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# print(list1.append(11))
# print(list1)
