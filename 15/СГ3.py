for a in range(2 ** 20):
    f = True
    for x in range(100000):
        if not((x & 57476 == 0) <= ((x & 90753 != 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)

