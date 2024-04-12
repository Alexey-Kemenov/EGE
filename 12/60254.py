def convert(s):
    while '55' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    return s


for n in range(3, 10001):
    a = '5' + '2' * n
    b = convert(a)
    if sum(map(int, list(b))) == 64:
        print(n)
