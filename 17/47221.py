f = open('47221.txt')
nums = list(map(int, f.readlines()))
n = 0
max = 0
count = 0
for i in nums:
    if i > n and i % 10 == 3:
        n = i

for j in range(len(nums) - 1):
    if ((abs(nums[j]) % 10 == 3) != (abs(nums[j + 1]) % 10 == 3)) and (nums[j] ** 2 + nums[j + 1] ** 2) >= n**2:
        count += 1

        a = nums[j] ** 2 + nums[j + 1] ** 2
        if a > max:
            max = a
print(count, max)
