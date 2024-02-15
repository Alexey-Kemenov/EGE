import itertools

liststring = itertools.product('ВИШНЯ', repeat=6)
count = 0
for str in liststring:
    a = ''.join(str)
    if a.count('В') <= 1 and str[0] != 'Ш' and str[5] != 'Я' and str[5] != 'И':
        count += 1
print(count)
