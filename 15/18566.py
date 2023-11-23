for a in range(100):
    f = True
    for m in range(100):
        for n in range(100):
            if not ((3 * m + 4 * n > 66) or ((m <= a) or (n < a))):
                f = False
    if f:
        print(a)
        break
