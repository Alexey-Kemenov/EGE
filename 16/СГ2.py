def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    if n % 2 != 0:
        return f(n // 10)


count = 0
for k in range(10 ** 9, 2 * 10 ** 9 + 1):
    s = str(k)
    if (s.count('2') + s.count('4') + s.count('6') + s.count('8')) == 0:
        count += 1
print(count)
