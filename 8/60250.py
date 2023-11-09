import itertools

ListString = itertools.permutations('01234567', 5)
count = 0
for str in ListString:
    line = ''.join(str)
    if line.count('1') == 0 and line[0] != '0':
        if int(line[0]) % 2 != int(line[1]) % 2 and int(line[1]) % 2 != int(line[2]) % 2 and int(line[2]) % 2 != int(
                line[3]) % 2 and int(line[3]) % 2 != int(line[4]) % 2:
            count += 1
            print(line)
print(count)
