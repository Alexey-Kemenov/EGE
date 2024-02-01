import itertools

ListString = itertools.permutations('ЯРОСЛАВ', 5)
count = 0
for str in ListString:
    line = ''.join(str)
    if line.count('Р') + line.count('С') + line.count('Л') + line.count('В') > line.count('Я') + line.count(
            'О') + line.count('А') and line.count(
        'ЯО') == 0 and line.count(
        'ОЯ') == 0 and line.count('ЯА') == 0 and line.count('АЯ') == 0 and line.count('ОА') == 0 and line.count(
        'АО') == 0:
        count += 1
print(count)
