for num in range(2, 1000):
    b = bin(num)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r > 396:
        print(r)
        break
