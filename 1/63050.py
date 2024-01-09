from itertools import permutations

table = '13 14 15 18 26 27 28 31 34 35 37 41 43 46 47 51 53 58 62 64 67 68 72 73 74 76 81 82 85 86'
graph = 'АБ БА АВ ВА ВД ДВ АГ ГА ГЕ ЕГ ДЕ ЕД ЕЖ ЖЕ ЕИ ИЕ ЖИ ИЖ ДИ ИД БИ ИБ АЖ ЖА БД ДБ БВ ВБ ГЖ ЖГ'
print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(1, 8 + 1):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(' '.join(p))