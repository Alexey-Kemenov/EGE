<<<<<<< HEAD
line = open('33196.txt').readlines()



=======
from collections import Counter

line = open('33196.txt').readline()

let = {}
max_count = 0
letter = ''

for i in range(len(line) - 1):
    if line[i] == 'A':
        if line[i + 1] in let:
            let[line[i + 1]] += 1
            if let[line[i + 1]] > max_count:
                max_count = let[line[i + 1]]
                letter = line[i + 1]
        else:
            let[line[i + 1]] = 1

print(letter)

#count = Counter(letters).most_common()[0]
#print(count)
>>>>>>> origin/master
