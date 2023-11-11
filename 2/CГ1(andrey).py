print('x y z w f1 f2')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f1 = (x == y) and (w <= z)
                f2 = (x <= y) <= (w == z)
                if f1 == 1:
                    print(x, y, z, w, int(f1), int(f2))
                
    