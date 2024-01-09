def od(n, m):
    for x in range(2, min(n, m) + 1):
        if n % x == 0 and m % x == 0:
            return True
    return False


for A in range(0, 100):
    f = True
    for x in range(0, 100):
        if not ((od(x, 42) <= (not od(x, 7))) or (x + A >= 25)):
            f = False
    if f:
        print(A)
        break
