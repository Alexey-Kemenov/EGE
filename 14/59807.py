for x in '0123456789ABCDEFG':
    res = int(f'8{x}5678', 25) + int(f'457{x}69', 25) + int(f'145{x}1', 25)
    if res % 23 == 0:
        print(res // 23)
