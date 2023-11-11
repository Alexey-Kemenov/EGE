def convert(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)
    return s


n = 61
while True:
    s = '1' * n
    if convert(s) == '2211':
        print(n)
        break
    n += 1
