def convert(s):
    while ' >1' in s or '>2' in s or '>0' in s:
        if ' >1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    return s


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for n in range(15):
    sum = 0
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    s = convert(s)
    for i in s:
        if i.isdigit():
            sum += int(i)
    if is_prime(sum):
        print(n)
