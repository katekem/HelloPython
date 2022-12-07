# def f(x):
#     x**2
# g = f
# print(type(f))
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2
# g = f
# print(f(2))

# def sum(x,y):
#     return x+y

# sum = lambda x, y: x + y

# def mult(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     return op(a,b)

# calc(sum, 4, 5)
# calc(lambda x, y: x + y, 4, 5)

## List comprehension
# [exp for item in iterable]
# [exp for item in iterable (if condition)]

# list = []
# for i in range(1,101):
#     # if(i%2 == 0):
#         list.append(i)
# print(list)

# list = [i for i in range(1,21) if i%2 == 0]
# print(list)

# list = [(i,i) for i in range(1,21) if i%2 == 0]
# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21) if i%2 == 0]
# print(list)


# В файле хранятся числа, нужно выбрать четные и составить список пар
# (число, квадрат числа)



# list = [1, 2, 3, 5, 8, 15, 23, 38]

# def f(x):
#     return x**2

# list2 = [(i, f(i)) for i in list if i%2 == 0]
# print(list2)

# # Решение

# path = '/Users/...file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e**2))

# print(out)


# # По-другому
# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# # Map

# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int,input().split()))
# print(data)

# data = map(int,'1 2 3 4 666 45'.split())
# for e in data:
#     print(e*10)

# print('--')

# for e in data:
#     print(e*10)


# # По-другому


def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)


## Filter
# Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для
# которых функция вернула True.

f(x) -> x - четное
filter(f, [1, 2, 3, 4, 5])
          [   2,    4   ]

# Нельзя пройтись дважды

data = [x for x in range(10)]
res = list(filter(lambda x: not x%2, data))
print(res)

# Напишем наш пример по-другому (заменим where):
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res)
print(res)


## Zip
# Функция zip() применяется к набору итерируемых объектов и возвращает 
# итератор с кортежами из элементов входных данных.
# Количество элементов в результате равно min количеству элементов входного
# набора.
# Нельзя пройтись дважды

zip ([1, 2, 3], ['o', 'd', 't'], ['f', 's', 't'])
[(1, 'o', 'f'), (2, 'd', 's'), (3, 't', 't')]


users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)


## Enumerate
# Функция enumerate() применяется к итерируемому объекту и возвращает 
# новый итератор с кортежами из индекса и элементов входных данных.
# Нельзя пройтись дважды

enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(ids))
print(data)





