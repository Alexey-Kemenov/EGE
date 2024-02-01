
for num in range(100, 200):
    b = bin(num)[2:]

    b += bin(num % 3)[2:].zfill(2)

    a = int(b, 2)
    b += bin(a % 5)[2:].zfill(3)
    r = int(b, 2)
    #if r >= 1111111110 and r <= 1444444416:
    print(num, r, r//num)
    