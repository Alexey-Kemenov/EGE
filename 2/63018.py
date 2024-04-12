print('u', 'w', 'x', 'y', 'z')
for u in range(2):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if not (((x <= y) and (z == (not w))) <= (u == (x or z))):
                        print(u, w, x, y, z)
