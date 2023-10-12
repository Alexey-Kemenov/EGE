for num in range(2, 1000):
    b = bin(num)[2:]
    l = len(b)
    if num % 3 == 0:
        b += b[-3:]
    else:
        a = (num % 3) * 3
        c = bin(a)[2:]
        b += c
    r = int(b, 2)
    if r > 76:
        print(num)
        break
