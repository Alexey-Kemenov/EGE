def f(x, y, z, w):
    if x == y:
        return 1
    if z:
        return f(x * 2, y, False, True)
    if w:
        return f(x + 1, y, True, False)
    if x > y:
        f(x + 1, y, True, False) + f(x * 2, y, False, True)


print(f(1, 14, True, False))
