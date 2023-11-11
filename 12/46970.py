def convert(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s


for x1 in range(20):
    for x2 in range(20):
        for x3 in range(20):
            s = '0' + x1 * '1' + x2 * '2' + x3 * '3' + '0'
            s = convert(s)
            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(x1+x2+x3+2)
                break
