def convert(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '320', 1)
        s = s.replace('03', '3012', 1)
    return s


for x1 in range(50):
    for x2 in range(50):
        for x3 in range(50):
            n = '0' + '1' * x1 + '2' * x2 + '3' * x3 + '0'
            n = convert(n)
            if n.count('1') == 26 and n.count('2') == 54 and n.count('3') == 48:
                print(2 + x1 + x2 + x3)
