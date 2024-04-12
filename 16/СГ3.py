def f(a, b):
    if b == 0:
        return 0
    if b > 0 and b % 2 == 0:
        return 2 * f(a, b / 2)
    if b % 2 != 0:
        return a + f(a, b - 1)


for x in range(1000):
    for y in range(1000):
        if f(x, y) == 89999 and x < y:
            print(y)
