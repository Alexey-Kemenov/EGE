def convert(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302')
        s = s.replace('02', '10')
        s = s.replace('03', '201')
    return s


for x1 in range(40):
    for x2 in range(40):
        for x3 in range(40):
            n = '0' + x1 * '1' + x2 * '2' + x3 * '3'
            n = convert(n)
            if n.count('1') == 40 and n.count('2') == 10 and n.count('3') == 8:
                print(x1)
                break
