import itertools

ListString = list(itertools.product('РЕГИНА', repeat=5))
count = 0
for str in ListString:
    line = ''.join(str)
    if line.count('Р') == 1 and line.count('Г') == 1 and line.count('Н') <= 1:
        count += 1
print(count)
