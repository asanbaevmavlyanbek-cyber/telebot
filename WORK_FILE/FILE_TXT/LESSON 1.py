"""
Файл TXT

'w' -> write ->Жазуу
'r' -> read -> окуу
'a' ->append -> кошуу

open() -> Файлдар мн иштоочу функция
with -> Автоматтык турдо файлды ачып кайра жабат
readline() -> Бир сапты окуйт
readlines() -> Бир нече сапты окуйт
close() -> Файлды жабат

"""
from datetime import datetime

# f = open('test.txt', 'w')
# f.write('Mavlyanbek\n')
# f.write('Asan\n')
# f.write('Uson\n')
# f.write('Maksat\n')
# f.close()

# a = open('test.txt', 'r')
# c = a.read()
# print(c)
# a.close()

# file = open('test.txt', 'r')
# for i in file:
#     print(i.strip())
# file.close()


# f = open('test.txt', 'a')
# f.write('Marat')
# f.close()


# with open('test.txt', 'r') as f:
#     a = f.read()
#     print(a)


# with open('bootcamp_48', 'w') as f:
#     f.write('Asan\nUson\nMarat\nMurat')

# with open('bootcamp_48', 'a') as f:
#     f.write('\nMavlyanbek Abdinasirovich')
#


# with open('bootcamp_48', 'r') as f:
#     a = f.readlines()
# print(a)
#
# print(len(a))


# text = input('Текст жаз: ')
# with open('user.txt', 'a') as f:
#     f.write(f'\n{text}')


# name = input('Атынды жаз: ')
#
# with open('user.txt', 'w') as f:
#     f.write(f'{datetime.now()} - {name}\n')
#
# print('Маалымат сакталды')