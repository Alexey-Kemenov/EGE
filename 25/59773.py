from fnmatch import fnmatch

for x in range(0, 10**8,1991):
     if fnmatch(str(x),'3?1*57'):
         print(x, x//1991)