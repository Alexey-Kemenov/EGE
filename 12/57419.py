def convert(s):
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    return s


for n in range(4, 1000):
    a = '2' + n * '5'
    a = convert(a)
    if sum(map(int, list(a))) == 17:
        print(n)
