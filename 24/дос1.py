line = open('дос1.txt').readline()
count = 0
max_count = 0
s1 = 'ABC'
s2 = '6789'
for i in range(len(line) - 1):
    if (line[i] in s1 and line[i + 1] in s2) or (line[i] in s2 and line[i + 1] in s1):
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 1

print(max_count)

# Альтернативный способ
line = line.replace('A', '*').replace('B', '*').replace('C', '*')
line = line.replace('6', '#').replace('7', '#').replace('8', '#').replace('9', '#')
# Могут быть случаи, когда подряд идёт больше двух букв или цифр, поэтому их также надо разделять в цикле
while '##' in line or '**' in line:
    line = line.replace('**', '* *').replace('##', '# #')
print(len(max(line.split(), key=len)))