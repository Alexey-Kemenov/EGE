line = open('38602.txt').readline()
while 'PP' in line:
    line = line.replace('PP', 'P P')
print(max(map(len, line.split())))