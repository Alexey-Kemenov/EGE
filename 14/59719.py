m = 100000000000
for x in '0123456789ABCDE':
    res = int(f'98{x}79641', 22) + int(f'25{x}49', 22) + int(f'63{x}5', 22)
    if res % 21 == 0:
        m = min(m, res)
print(m // 21)
