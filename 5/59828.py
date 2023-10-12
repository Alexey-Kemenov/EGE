def three(n):
    t = ''
    while n > 0:
        a = str(n % 3)
        t += a
        n //= 3
        t = t[::-1]
    return t


for num in range(2, 1000):
    b = three(num)
    if num % 3 == 0:
        b += b[-3:]
    else:
        a = three(num % 3 * 3)
        b += a
    r = int(b, 3)
    if r > 150:
        print(num)
        break
