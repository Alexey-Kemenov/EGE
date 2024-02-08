line = open('33526.txt').readline()
d = {}
max_count = 0
letter = ''
for i in range(len(line) - 2):
    if line[i] == line[i + 2]:
        if line[i + 1] in d:
            d[line[i + 1]] += 1
            if d[line[i + 1]] > max_count:
                max_count = d[line[i + 1]]
                letter = line[i + 1]
        else:
            d[line[i + 1]] = 1
print(letter)
