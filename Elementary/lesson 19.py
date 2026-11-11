"""
*args **kwargs -> Парметр
*args -> Аргумент
**kwargs -> ключ аргумент
*args -> tuple()
**kwargs -> dict{}

"""

# def person(*args):
#     print(args)
#
# person(1, 2, 3)

#
# def student(*args):
#     print(args[1])
#
# student('Mavlyanbek', 'ASAN', 'uson')
#


# def add_nambers(*arge):
#     t = 8
#     for i in arge:
#         t += 1
#         return t
# print(add_nambers(1, 2, 3))

# def info(*args):
#     print(f'Биринчи аргумент'[1])





# 1
# def name(*args):
#     for i in args:
#       print('Hello:', i)
# name('Asan', 'Uson', 'Marat', 'Murat')

# 2
# def sum_nambers(*args):
#     print(sum(args))
# sum_nambers(1, 2, 3, 4, 5)

# 3
# def info(*args):
#     print(args)
# info(1, 3, 'Asan', 25)


# 4
# def nambers(*args):
#     print(max(args))
# nambers(1, 2, 3, 4, 5, 6, 7, 8, 10)


# 5
# def students(*args):
#     for i in args:
#         print('student:', i)
# students('Asan', 'Uson')

# 6
# def info(**kwargs):
#     print(kwargs)
#
# info(name= 'Asan', age=20, city='Talas')

# 7
# def products(**kwargs):
#     print(kwargs)
# products(name= 'apple', price= 100, category= 'good')

# 8
# def info(**kwargs):
#     print(kwargs)
#
# info(name= 'Asan', age= 22, hobbi= 'football')

# 9
# def info(*args, **kwargs):
#     print('Сандар:', args)
#     print('Адам тууралуу маалымат:', kwargs)
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# info(1, 5, 8, name='Asan', age= 22, name1='Uson', age1=25)

# 10
# def hobbi_info(*args, **kwargs):
#     print('Хоббиси:', args)
#     print('Адам жонундо маалымат:', kwargs)
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# hobbi_info('volleyball', 'football', 'swimming', name='Asan', age= 20, city= 'Bishkek')

