for num in range(100):
    a = bin(num)[2:]
    if num % 2 == 0:
        a += '01'
    if num % 2 != 0:
        a += '1'
        a = a[::-1]
        a += '1'
        a = a[::-1]
    r = int(a, 2)
    if r > 156:
        print(num)
        break
