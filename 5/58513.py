def convert(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b += bin(5)[2:]
    else:
        b += '1'
    if int(b, 2) % 7 == 0:
        b += bin(7)[2:]
    else:
        b += '1'
    return b


for num in range(2, 1000000):
    a = convert(num)
    r = int(a, 2)
    if r < 1855663:
        print(num)
