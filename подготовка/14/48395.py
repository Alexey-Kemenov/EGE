for x in '0123456789':
    b = int(f'28{x}2', 18) + int(f'93{x}5', 12)
    if b % 133 == 0:
        a = b // 133
print(a)
