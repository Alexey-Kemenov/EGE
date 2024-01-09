for num in range(2, 1000):
    b = bin(num)[2:]
    if num % 3 == 0:
        a = b[-3:]
        b += a
    if num % 3 != 0:
        s = (num % 3) * 3
        b += bin(s)[2:]
    r = int(b, 2)
    if r < 170:
        print(r)
