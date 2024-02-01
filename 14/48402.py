m = 1000000
for x in '0123456789':
    res = int(f'3{x}DA', 14) + int(f'5{x}A6', 12)
    if res % 81 == 0:
        m = min(m, res)
print(m // 81)
