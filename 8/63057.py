import itertools

ListString = itertools.product('012345678', repeat=9)
count = 0
for i1 in '2468':
    for i2 in '1357':
        for i3 in '2468':
            for i4 in '1357':
                for i5 in '2468':
                    for i6 in '1357':
                        for i7 in '2468':
                            for i8 in '1357':
                                for i9 in '2468':
                                    a = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9
                                    if a.count('0') == 0 and a.count('1') <= 3 and a.count('2') <= 3 and a.count(
                                            '3') <= 3 and a.count(
                                        '4') <= 3 and a.count('5') <= 3 and a.count('6') <= 3 and a.count(
                                        '7') <= 3 and a.count('8') <= 3:
                                        count += 1
print(count*2)
