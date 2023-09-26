print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # Если функция в задании (в последнем столбце) равна нулю,
                # то всё выражение помещаем под отрицание not()
                if not((x and not(y)) or (y == z) or w):
                    print(x, y, z, w)
