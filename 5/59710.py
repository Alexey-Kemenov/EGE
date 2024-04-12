for num in range(100):
    b = bin(num)[2:]
    if num % 3 == 0:
        a = b[-3:]
        b += a
    if num % 3 != 0:
        a = 3 * (num % 3)
        a = bin(a)[2:]
        b += a
    r = int(b, 2)
    if r >= 76:
        print(num)
