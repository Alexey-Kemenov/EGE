f = open('дос 1.txt')
line = list(map(int,f.readlines()))
n = 0
count = 0
max = 0
for i in line:
    if i > n and i % 19 == 0:
        n = i

for j in range(len(line) - 1):
    if (line[j] > n and line[j + 1] < n) or (line[j] < n and line[j + 1] > n) or (line[j] > n and line[j + 1] > n):
        count += 1
        a = line[j] + line[j + 1]
        if a > max:
            max = a
print(count, max)
