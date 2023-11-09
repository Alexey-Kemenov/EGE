print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f_1 = (x == y) and (w <= z)
                f_2 = (x <= y) <= (w == z)
                if (not f_1 and ([x, y, z, w].count(1) == 1)) or f_1:
                    if (not f_2 and ([x, y, z, w].count(1) == 1)) or f_2:
                        print(x, y, z, w, int(f_1), int(f_2))
