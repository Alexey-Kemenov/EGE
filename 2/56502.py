print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((x <= y) or (z <= w)) and ((z == y) <= (w == x))):
                    print(x, y, z, w)
