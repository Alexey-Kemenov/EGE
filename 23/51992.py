# Ограничение "никакая команда не повторяется более двух раз подряд"
def f(x, y, cur, pre):
    if x > y:
        return 0
    if x == y:
        return 1
    if pre == cur == '+':
        return f(x * 2, y, '*', cur)
    elif pre == cur == '*':
        return f(x + 1, y, '+', cur)
    else:
        return f(x * 2, y, '*', cur) + f(x + 1, y, '+', cur)

print(f(1, 16, '', ''))
