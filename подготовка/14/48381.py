for x in '0123456789ABCD':
    M = int(f'8{x}12{x}', 14)
    N = int(f'8{x}542', 14)
    for A in range(1, 1000):
        if (M + A) % N == 0:
            print(A)
            break

