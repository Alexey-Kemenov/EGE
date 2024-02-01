from itertools import product

# До этого с помощью рекурсивной функции определили то, что функция возвращает 0, когда в числе нет чётных цифр.

count = 0
for num in product('013579', repeat=10):
    if num[0] != '0' and num[0] in '12':
        count += 1

print(count)

# 10 077 696