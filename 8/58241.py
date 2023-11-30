import itertools

ListString = itertools.product('012345', repeat=3)
count = -1
for str in ListString:
    line = ''.join(str)
    if max(str) == str[0] and min(str) == str[2]:
        count += 1
print(count)
