for x in '0123456789ABCDEFGHI':
    b = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if b % 18 == 0:
        a = b // 18
print(a)
