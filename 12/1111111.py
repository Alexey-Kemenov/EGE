def convert(s):
    while '52' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    return s


for n in range(2, 100000):
    a = '5' + n * '2'
    a = convert(a)
    if a.count('1') + a.count('5') * 5 + a.count('2') * 2 == 64:
        print(n)
