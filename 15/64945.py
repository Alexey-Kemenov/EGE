for a in range(32768):
    f = True
    for x in range(32768):
        if not((x&21074!=0) <= ((x&12369 == 0) <= (x&a !=0))):
            f = False
    if f:
        print(a)
        break
