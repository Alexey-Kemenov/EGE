def f(x, y):
    if x == y:
        return 1
    if x > y :
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x + 3, y)

# Ограничение "траектория содержит число n"
# f(начало, n) * f(n, конец)

print(f(2, 10) * f(10, 14))