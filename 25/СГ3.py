from fnmatch import fnmatch

for x in range(0, 10 ** 9, 9517):
    if fnmatch(str(x),'2*41*6?9'):
        print(x,x//9517)
