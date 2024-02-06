def f(x, y, c1, c2, c3):
    if x > y:
        return 0
    if x == y:
        return c1 <= 4 and c2 >= 2 and c3 == 5
    return f(x * 5, y, c1 + 1, c2, c3) + f(x * 3, y, c1, c2 + 1, c3) + f(x + 45, y, c1, c2, c3 + 1)

print(f(1, 2970, 0, 0, 0))