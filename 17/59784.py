f = open('59784.txt')
nums = list(map(int, f.readlines()))
count = 0
min = 1000000
n = 0
for i in nums:
    if i > n and abs(i) % 100 == 15:
        n = i
for j in range(len(nums) - 2):
    if (len(str(abs(nums[j]))) == 4 and len(str(abs(nums[j + 1]))) != 4 and len(str(abs(nums[j + 2]))) != 4) or (
            len(str(abs(nums[j]))) != 4 and len(str(abs(nums[j + 1]))) == 4 and len(str(abs(nums[j + 2]))) != 4) or (
            len(str(abs(nums[j]))) != 4 and len(str(abs(nums[j + 1]))) != 4 and len(str(abs(nums[j + 2]))) == 4):
        if (nums[j] + nums[j + 1] + nums[j + 2]) < n:
            count += 1
            a = (nums[j] + nums[j + 1] + nums[j + 2])
            if a < min:
                min = a

print(count, min)


