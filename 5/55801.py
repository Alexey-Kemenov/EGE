for num in range(2, 1000):
    b = bin(num)[2:]
    if num % 3 == 0:
        b += b[-3:]
    if num % 3 != 0:
        c = bin(3 * (num % 3))[2:]
        b += c
    r = int(b, 2)
    if r < 100:
        print(num)
