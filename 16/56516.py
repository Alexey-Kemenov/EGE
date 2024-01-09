import sys

sys.setrecursionlimit(50000)


def f(a, b):
    if b == 0:
        return a
    if a >= b:
        return f(a - 1, b) + b
    if a < b and b > 0:
        return f(a, b - 1) + a


count = 0
for a in range(1, 1048576 + 1):
    if 1048576 % a == 0:
        count += 1
print(count)
