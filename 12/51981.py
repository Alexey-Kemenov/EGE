import itertools


def convert(s):
    while '00' not in s:
        s = s.replace('012', '30', 1)
        if '011' in s:
            s = s.replace('011', '20', 1)
            s = s.replace('022', '40', 1)
        if '011' not in s:
            s = s.replace('01', '10', 1)
            s = s.replace('02', '101', 1)
    return s


a = itertools.product('12', repeat=20)
for str in a:
    line = ''.join(str)
    c = '0' + line + '0'
    if c.count('1')==10 and c.count('2')==10:
        b = convert(c)
        if b.count('1') == 7 and b.count('2') == 5:
            print(b.count('3'))
            break
