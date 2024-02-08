line = open('33526.txt').readline()
d = {}
count = 0
for j in range(len(line) - 2):
    if str(line[j]) == str(line[j + 2]):
