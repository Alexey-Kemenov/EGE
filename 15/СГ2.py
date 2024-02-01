for a in range(150):
    f = True
    for x in range(150):
        if not ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0):
            f = False
    if f:
        print(a)
        break