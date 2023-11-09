import itertools

ListString = itertools.permutations('ЛЕВИЙ')
count = 0
for str in ListString:
    line = ''.join(str)
    if line[0] != 'Й' and line.count('ЕИ') == 0:
        count += 1
print(count)
