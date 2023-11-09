import itertools

ListString = itertools.product('АКРУ', repeat=5)
count = 0
for str in ListString:
    count += 1
    line = ''.join(str)
    if line == 'УКАРА':
        break
print(count)
