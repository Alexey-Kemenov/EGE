for A in range(0, 1000):
    f = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((x + 2 * y < A) or (y > x) or (x > 60)):
                f = False
    if f:
        print(A)
        break
