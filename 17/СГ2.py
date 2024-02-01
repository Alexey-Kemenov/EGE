f = open('СГ2.txt')
nums = (list(map(int, f.readlines())))
n = 0
max= 0
count = 0
for i in nums:
    if i > n and i % 1000 == 123:
        n = i

for j in range(len(nums) - 2):
    if ((len(str(nums[j])) == 5 and len(str(nums[j + 1])) == 5) or (
            len(str(nums[j])) == 5 and len(str(nums[j + 2])) == 5) or (
                len(str(nums[j + 1])) == 5 and len(str(nums[j + 2])) == 5)) and ((
            nums[j] % 3 == 0 and nums[j + 1] % 3 != 0 and nums[j + 2] % 3 != 0) or (
            nums[j] % 3 != 0 and nums[j + 1] % 3 == 0 and nums[j + 2] % 3 != 0) or (
            nums[j] % 3 != 0 and nums[j + 1] % 3 != 0 and nums[j + 2] % 3 == 0)) and nums[j]+nums[j+1]+nums[j+2]>n:
        count+=1
        a = nums[j] + nums[j + 1] + nums[j + 2]
        if a > max:
            max = a
print(count, max)




