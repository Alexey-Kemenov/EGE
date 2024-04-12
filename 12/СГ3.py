def convert(s):
    while '00' not in s:
        s = s.replace('011', '201', 1)
        s = s.replace('03', '220', 1)
        s = s.replace('02', '210', 1)
        s = s.replace('012', '2101', 1)
        s = s.replace('013', '12101', 1)
        s = s.replace('010', '1100', 1)
    return s


print(sum(map(int,list('012110'))),sum(map(int,list(convert('012110')))))
