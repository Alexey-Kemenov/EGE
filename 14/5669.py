for x in '0123456789ABCDEF':
    a = int(f'8569{x}', 16) + int(f'12{x}48', 16)
    d = ''
    while a != 0:
        d = str(a % 8) + d
        a = a // 8
    if d.count('0') + d.count('2') + d.count('4') + d.count('6') <= 2:
        print(d)

