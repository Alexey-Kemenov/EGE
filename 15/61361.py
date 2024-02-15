for a in range(100):
    f = False
    for x in range(100):
        for y in range(100):
            if not ((x + 2 * y > 48) or (y > x) or (x + 3 * y < a)):
                f = True
    if f:
        print(a)

