f = open('59695.txt')
nums = list(map(int, f.readlines()))
count = 0
max = 0
n = 0
for i in nums:
    if i > n and i % 100 == 15:
        n = i
for j in range(len(nums) - 2):
    if (len(str(nums[j])) != 4 and len(str(nums[j + 1])) != 4 and len(str(nums[j + 2])) == 4) or (len(
            str(nums[j])) != 4 and len(
        str(nums[j + 1])) == 4 and len(str(nums[j + 2])) != 4) or (len(str(nums[j])) == 4 and len(
        str(nums[j + 1])) != 4 and len(str(nums[j + 2])) != 4):
        if (nums[j] + nums[j + 1] + nums[j + 2]) >= n:
            count += 1
            a = nums[j] + nums[j + 1] + nums[j + 2]
            if a > max:
                max = a
print(count, max)
