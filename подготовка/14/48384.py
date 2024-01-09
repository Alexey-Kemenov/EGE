for x in '012345678':
    for y in '012345678':
        b = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        if b % 61 == 0:
            a = b // 61
print(a)
