def sum(n):
    a = 0
    while n > 0:
        a += n % 10
        n //= 10
    return a


for num in range(1, 1000):
    b = bin(num)[2:]
    if sum(num) % 2 != 0:
        b += '1'
    if sum(num) % 2 == 0:
        b += '0'
    if sum(int(b, 2)) % 2 != 0:
        b += '1'
    if sum(int(b, 2)) % 2 == 0:
        b += '0'
    if sum(int(b, 2)) % 2 != 0:
        b += '1'
    if sum(int(b, 2)) % 2 == 0:
        b += '0'
    r = int(b, 2)
    print(num, r, r//num)

"""
    count = 0
    for i in range(123456789, 1987654322):
        if i == r:
            count += 1
print(count)
"""
