f = open('17(2).txt')
nums = list(map(int, f.readlines()))
n = 0
count = 0
max = 0
for j in range(len(nums) - 2):
    if (len(str((nums[j + 1]))) == 3 and int(nums[j + 1]) > 0 and int(nums[j + 1]) % 2 != 0):
        count += 1
        a = nums[j] + nums[j + 1] + nums[j + 2]
        if a > max:
            max = a
print(count, max)
