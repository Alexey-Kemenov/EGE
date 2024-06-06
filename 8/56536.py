from itertools import product

all = product('?!', repeat=12)
odd = 0
even = 0
for i in all:
    s = ''.join(i)
    if s.count('!!') == 0 and s.count('!') == 3:
        if s[0] == '!':
            odd += 1
        else:
            even += 1
# Чётное "0246"
# Нечётное "1357"
print((4**12)*odd + 3*(4**11)*even)