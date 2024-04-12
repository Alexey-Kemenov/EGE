def f(x, y, count):
    if x == y and count <= 4:
        return 1
    if x > y:
        return 0
    if x % 2 == 0:
        count += 1
    return f(x + 1, y, count) + f(x * 2, y, count)


print(f(1, 19, 0))
