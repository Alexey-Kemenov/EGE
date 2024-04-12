count = 0
for num in range(1,1000):
    b = bin(num)[2:]
    a = num % 3
    a = bin(a)[2:].zfill(2)
    b += a
    c = int(b, 2)
    c = bin(c % 5)[2:].zfill(3)
    b += c
    r = int(b, 2)
    count+=1
    print(num, r, r // num, b,count)
    # if 1111111110 <= r <= 1444444417:
    #   print(num)
