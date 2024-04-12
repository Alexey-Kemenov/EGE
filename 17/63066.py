f = open('63066.txt')
s = list(map(int, f.readlines()))
n = 0
count = 0
max = 0
for i in s:
    if i > n and n % 1000 == 321:
        n = i
for j in range(len(s) - 2):
    if ((len(str(s[j])) == 5 and len(str(s[j + 1])) == 5 and len(str(s[j + 2])) != 5) or (len(str(s[j])) == 5 and len(
            str(s[j + 1])) != 5 and len(str(s[j + 2])) == 5) or (
                len(str(s[j])) != 5 and len(str(s[j + 1])) == 5 and len(str(s[j + 2])) == 5)) and ((s[j] % 5 == 0 and s[
        j + 1] % 5 != 0 and s[j + 2] % 5 != 0) or (s[j] % 5 == 0 and s[j + 1] % 5 == 0 and s[j + 2] % 5 != 0) or (s[
        j] % 5 == 0 and s[j + 1] % 5 == 0 and s[j+2]%5==0) or (s[j]%5!=0 and s[j+1]%5==0 and s[j+2]%5==0) or ( s[j]%5!=0 and  s[
        j + 1] % 5 != 0 and s[j+2]%5==0) or (s[j]%5!=0 and s[j + 1] % 5 == 0 and s[j + 2] % 5 != 0) or (s[j] % 5 == 0 and  s[
        j + 1] % 5 != 0 and s[j+2]%5==0)):
        if s[j] + s[j+1] + s[j+2]>n:
            count+=1
            a = s[j]+s[j+1]+s[j+2]
            if a> max:
                max=a
print(count,max)



