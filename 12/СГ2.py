import itertools


def convert(s):
    while '00' not in s:
        s = s.replace('01', '220', 1)
        s = s.replace('02', '1013', 1)
        s = s.replace('03', '120', 1)
    return s


for x1 in range(20):
    for x2 in range(20):
        for x3 in range(20):

            a = '0' + '1' * x1 + '2' * x2 + '3' * x3 + '0'
            a = convert(a)
            """
            c = itertools.permutations(a)
            for str in c:
                d = ''.join(str)
                k = '0' + d + '0'
                b = convert(k)
             """
            if a.count('1') == 13 and a.count('2') == 18:
                print(x1 + x2 + x3 + 2)
