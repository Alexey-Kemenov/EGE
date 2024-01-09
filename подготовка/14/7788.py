a = 4 ** 2018 + 2 ** 2018 - 32
a = bin(a)[2:]
a = str(a)
print(a.count('1'))
