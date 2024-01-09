
f = open('10100.txt')
nums = list(map(int, f.readlines()))
n = 0
count = 0
max = 0
for i in nums:
    if i > n and i % 100 == 13:
        n = i
for j in range(len(nums) - 2):
    if (len(str(nums[j])) == 3 and len(str(nums[j + 1])) == 3 and len(str(nums[j + 2])) != 3) or (
            len(str(nums[j])) == 3 and len(str(nums[j + 1])) != 3 and len(str(nums[j + 2])) == 3) or (
            len(str(nums[j])) != 3 and len(str(nums[j + 1])) == 3 and len(str(nums[j + 2])) == 3):
        if nums[j] + nums[j + 1] + nums[j + 2] <= n:
            count += 1
            a = nums[j] + nums[j + 1] + nums[j + 2]
            if a > max:
                max = a
print(count, max)