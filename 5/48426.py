for num in range(2, 10000):
    b = bin(num)[2:]
    b = b.replace('1', '*').replace('0', '1').replace('*', '0')
    r = int(b, 2)
    if num - r == 999:
        print(num)
        break
