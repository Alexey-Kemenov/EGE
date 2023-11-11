import itertools

print(list(itertools.product('ABC', 'abc')))
# [('A', 'a'), ('A', 'b'), ('A', 'c'), ('B', 'a'), ('B', 'b'), ('B', 'c'), ('C', 'a'), ('C', 'b'), ('C', 'c')]
print(list(itertools.product('ABC', repeat=3)))

import itertools

listString = itertools.product('БОРИС', repeat=6)
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)