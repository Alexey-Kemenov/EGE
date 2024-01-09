import itertools

ListString = itertools.product('МЕТРО', repeat=4)
count = 0
for str in ListString:
    line = ''.join(str)
    if (line[0] == 'М' or line[0] == 'Т' or line[0] == 'Р') and (line[3] == 'Е' or line[3] == 'О'):
        count += 1
print(count)
