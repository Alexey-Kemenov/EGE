for x in '0123456':
    for y in '0123456':
        b = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if b % 181 == 0:
            a = b // 181
print(a)
