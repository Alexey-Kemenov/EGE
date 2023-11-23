f = open('58525.txt')
nums = list(map(int, f.readlines()))
m = 20000
count = 0
max = 0
for i in nums:
    s = str(i)
    if i < m and len(s) == 3 and i % 10 == 3:
        m = i
for j in range(len(nums) - 1):
    if len(str(nums[j])) == 4 and len(str(nums[j + 1])) != 4 or len(str(nums[j])) != 4 and len(str(nums[j + 1])) == 4:
        if (nums[j] ** 2 + nums[j + 1] ** 2) % m == 0:
            count += 1
            a = (nums[j] ** 2 + nums[j + 1] ** 2)
            if a > max:
                max = a
print(count, max)
