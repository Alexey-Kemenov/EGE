import itertools

ListString = itertools.product('НИКОЛАЙ', repeat=4)
count = 0
for str in ListString:
    line = ''.join(str)
    if line[0] != 'Й' and (line.count('И') >= 1 or line.count('А') >= 1 or line.count('О') >= 1):
        count += 1
print(count)
