for num in range(1, 10000):
    b = bin(num)[2:]
    a = ''
    for i in b:
        if i == '1':
            a += '0'
        if i == '0':
            a += '1'
    if a[0] == '0' and a.count('1') > 0:
        a = a.lstrip('0')
    a = int(a, 2)
    r = num - a
    if r == 979:
        print(num)
