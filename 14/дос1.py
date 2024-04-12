for x in '0123456789ABCDEFGHIJKLMNOPQ':
    res = int(f'123{x}24', 27) + int(f'135{x}78', 27)
    if res % 26 == 0:
        print(res // 26)
