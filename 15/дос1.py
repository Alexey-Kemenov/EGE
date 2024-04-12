for Aa in range(200):
    for Ab in range(200):
        f = True
        for x in range(500):
            if not ((x in range(47, 116)) <= (
                    (x not in range(Aa, Ab+1)) and (x in range(24, 91))) <= (x not in range(47, 116))):
                f = False
    if f:
        print(Aa, Ab)
