for num in range(2, 1000):
    b = bin(num)[2:]
    if num % 3 == 0:
        b += b[-3:]
    if num % 3 != 0:
        b += bin((num % 3) * 3)[2:]
    r = int(b, 2)
    if r > 151:
        print(r)
