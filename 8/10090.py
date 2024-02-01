import itertools

ListString = itertools.permutations('0234567', 5)
count = 0
for str in ListString:
    line = ''.join(str)
    if (line.count('24') == 0 and line.count('26') == 0 and line.count('42') == 0 and line.count(
            '46') == 0 and line.count('62') == 0 and line.count('64') == 0 and line.count('20') == 0 and line.count(
        '40') == 0 and line.count('60') == 0 and line.count('02') == 0 and line.count('04') == 0 and line.count(
        '06') == 0) and (
            line.count('35') == 0 and line.count(
        '37') == 0 and line.count('53') == 0 and line.count('57') == 0 and line.count('73') == 0 and line.count(
        '75') == 0) and line[0] != '0':
        count += 1
    print(line)
    print(count)
