for num in range(2, 1000):
    b = bin(num)[2:]
    if num % 2 == 0:
        b += '0'
        a = b[::-1]
        a += '1'
        b = a[::-1]
    if num % 2 != 0:
        b += '11'
        a = b[::-1]
        a += '11'
        b = a[::-1]
    r = int(b, 2)
    if r > 52:
        print(r)
