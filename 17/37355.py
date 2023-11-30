f = open('37355.txt')
nums = list(map(int, f.readlines()))
count = 0
max = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 7 == 0:
            count += 1
            a = (nums[i] + nums[j])
            if a > max:
                max = a
print(count, max)
