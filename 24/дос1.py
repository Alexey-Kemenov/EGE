line = open('дос1.txt').readline()
count = 0
max = 0
s1 = 'ABC'
s2 = '6789'
for i in range(len(line) - 1):
    if (line[i] in s1 and line[i + 1] in s2) or (line[i] in s2 and line[i + 1] in s1):
        count += 1
        if count > max:
            max = count
    else:
        count = 1

print(max)
