f = open('СГ3.txt')
nums = list(map(int, f.readlines()))
n = 0
c = 0
count = 0
max = 0
min = 0
sum = 0
for i in nums:
    if i > n and i % 1000 == 652:
        n = i
        max = n

for j in nums:
    if j < n and j % 1000 == 652:
        n = j
        min = n

for a in range(len(nums) - 3):
    x5 = [len(str(nums[a])) == 5, len(str(nums[a + 1])) == 5, len(str(nums[a + 2])) == 5,
          len(str(nums[a + 3])) == 5].count(True)
    x4 = [len(str(nums[a])) == 4, len(str(nums[a + 1])) == 4, len(str(nums[a + 2])) == 4,
          len(str(nums[a + 3])) == 4].count(True)
    x3 = [nums[a] % 3 == 0, nums[a + 1] % 3 == 0, nums[a + 2] % 3 == 0, nums[a + 3] % 3 == 0].count(True)
    x7 = [nums[a] % 7 == 0, nums[a + 1] % 7 == 0, nums[a + 2] % 7 == 0, nums[a + 3] % 7 == 0].count(True)
    if x5 > x4 and x3 == x7 and (nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3]) > (max + min) * 2:
        count += 1

        s = nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3]
        if s > sum:
            sum = s
print(count, sum)
