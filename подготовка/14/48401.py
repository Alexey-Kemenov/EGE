for x in '0123456789':
    b = int(F'{x}A04', 13) + int(f'1D{x}3', 18)
    if b % 184 == 0:
        a = b // 184
print(a)
