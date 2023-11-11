m = 99999999
for x in '01234567':
    for y in '01234567':
        res = int(f'{x}01{y}4', 9) + int(f'{x}{y}544', 8)
        if res % 89 == 0:
            m = min(m, res)
print(m // 89)
