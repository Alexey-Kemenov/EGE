def f(n):
    if n < 3:
        return 1
    if n > 2:
        a = 0
        for i in range(1, n):
            a += f(i)
        return a


print(f(18))
