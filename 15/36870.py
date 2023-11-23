for a in range(50):
    f = True
    for x in range(50):
        if not ((x & 49 == 0) <= ((x & 28 != 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)
        break
