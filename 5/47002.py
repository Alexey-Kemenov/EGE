for n in range(2, 500):
    b = bin(n)[2:]
    z = b[0::2].count('0')
    o = b[1::2].count('1')
    if abs(z - o) == 4:
        print(n)
        break
