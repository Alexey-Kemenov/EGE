import itertools

ListString = itertools.product('АВЕСТ', repeat=5)
count = 0
for str in ListString:
    count += 1
    line = ''.join(str)
    if line == 'СВЕТА':
        break
print(count)
