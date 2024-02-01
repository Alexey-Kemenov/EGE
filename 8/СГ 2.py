"""

import itertools

ListString = itertools.product('012345678', repeat=11)
count = 0
for str in ListString:
    line = ''.join(str)
    if line.count('0') == 0
"""
count = 0
for i1 in '2468':
    for i2 in '1357':
        for i3 in '2486':
            for i4 in '1357':
                for i5 in '2468':
                    for i6 in '1357':
                        for i7 in '2468':
                            for i8 in '1357':
                                for i9 in '2468':
                                    for i10 in '1357':
                                        for i11 in '2468':
                                            a = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11
                                            if a.count('1') <= 4 and a.count('2') <= 4 and a.count(
                                                    '3') <= 4 and a.count('4') <= 4 and a.count('5') <= 4 and a.count(
                                                '6') <= 4 and a.count('7') <= 4 and a.count('8') <= 4:
                                                count += 1
print(count)