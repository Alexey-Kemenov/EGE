f = open('59722.txt')
nums = list(map(int, f.readlines()))
n = 0
count = 0
for i in nums:
    if i > n and i % 100 == 17:
        n = i

for j in range(len(nums) - 2):
    if ((len(str(abs(nums[j]))) == 3 and len(str(abs(nums[j + 1]))) != 3 and len(str(abs(nums[j + 2]))) != 3) or \
            (len(str(abs(nums[j]))) != 3 and len(str(abs(nums[j + 1]))) == 3 and len(str(abs(nums[j + 2]))) != 3) or \
            (len(str(abs(nums[j]))) != 3 and len(str(abs(nums[j + 1]))) != 3 and len(str(abs(nums[j + 2]))) == 3)) and \
            nums[j] + nums[j + 1] + nums[j + 2] < n:
        count += 1
print(count)
