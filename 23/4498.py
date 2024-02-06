s = set()


def f(x, step1, step2, step3, y):
    if step1 <= 4 and step2 >= 2 and step3 == 5:
        if x == 2970:
            y.add(x)
    else:
        f(x * 5, step1 + 1, step2, step3, y)
        f(x * 3, step1, step2 + 1, step3, y)
        f(x + 45, step1, step2, step3 + 1, y)


f(1, 0, 0, 0,s)
print(f(1,2970))
