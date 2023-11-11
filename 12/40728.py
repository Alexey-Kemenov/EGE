def convert(s):
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    return s


for i in range(200, 250):
    s = '1' * i
    s = convert(s)
    print(s)

#Ответ:201