"""""
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    if n % 2 != 0:
        return f(n // 10)


for k in range(1,1000):
    print(k,f(k))
""""""
"""""
"""""
count = 0
for k in range(10 ** 9, 2 * 10 ** 9+1):
    if f(k) == 2:
        count+=1
        print(f(k),k,count)
"""""
import itertools

liststring = itertools.product('0123579', repeat=10)
count = 0
for str in liststring:
    a = ''.join(str)
    if a.count('2') == 1 and a[0] == '1':
        count += 1
print(count)
