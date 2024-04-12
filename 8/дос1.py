import itertools

count = 0
Liststring = itertools.product('АПРСУ', repeat=5)
for str in Liststring:
    count += 1
    a = ''.join(str)
    if a.count('У') <= 1 and a.count('АА') == 0:
        break

print(count)
