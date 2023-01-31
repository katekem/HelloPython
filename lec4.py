# # # Написать программу сложения двух чисел

# # Вариант самый простой
# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {x + y}')

# # Метод
def sum(a, b):
    return a + b
x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {sum(x, y)}')

# # Lambda
sum = lambda a, b: a + b
x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {sum(x, y)}')

