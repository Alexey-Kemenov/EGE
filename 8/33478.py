import itertools

ListString = itertools.product('АНДРЕЙ', repeat=6)
count = 0
for str in ListString:
    line = ''.join(str)
    if line.count('Й') <= 1 and line[0] != 'Й' and line[-1] != 'Й' and line.count('ЕЙ') == 0 and line.count('ЙЕ') == 0:
        count += 1
    else:
        count += 0

print(count)
