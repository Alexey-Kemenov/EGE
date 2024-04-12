def convert(s):
    while '1111' in s or '8888' in s:
        if '1111' in s:
            s = s.replace('1111', '88', 1)
        if '1111' not in s:
            s = s.replace('8888', '11', 1)
    return s


a = 45 * '8'
print(convert(a))
