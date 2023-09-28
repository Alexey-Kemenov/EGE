print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w <= (y == z)) and (y == (z <= x))
                # Если f равно false и среди переменных ровно одна единица или f равно true
                if (not f and ([x, y, z, w].count(1) == 1)) or f:
                    print(x, y, z, w, int(f))
