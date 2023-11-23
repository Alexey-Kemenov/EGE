for a in range(500):
    f = True
    for x in range(500):
        for y in range(500):
            if not ((48 != y + 2 * x) or (a < x) or (a < y)):
                f = False
    if f:
        print(a)

