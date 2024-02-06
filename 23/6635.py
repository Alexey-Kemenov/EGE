# Ограничение "содержится ровно 13 команд"
s = set()
def f(x, step, nums):
    if step == 13:
        if x < 0:
            nums.add(x)
    else:
        f(x - 3, step + 1, nums)
        f(x * -3, step + 1, nums)

f(333, 0, s)
print(len(s))