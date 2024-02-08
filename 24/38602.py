<<<<<<< HEAD
f = open('24.txt')
nums = list(map(int, f.readlines))

=======
line = open('38602.txt').readline()
while 'PP' in line:
    line = line.replace('PP', 'P P')
print(max(map(len, line.split())))
>>>>>>> origin/master
