line = open('59848.txt').readline()
s = '0123456789ABCDEFGHIJKLMN'
count = 0
max = 0
a = ''
for i in range(len(line)):
    if line[i] in s:
        count += 1
        if count > max:
            max = count
    if line[i] not in s:
        count = 0
print(max)
