f = open('17(stepik).txt')
nums = list(map(int, f.readlines()))
count = 0
for j in range(len(nums) - 1):
    if (int(abs(nums[j])) % 10 == 7 and int(abs(nums[j + 1])) % 10 == 7) or (
            int(abs(nums[j])) % 10 == 7 and int(abs(nums[j + 1])) % 10 != 7) or (int(abs(nums[j])) % 10 != 7 and int(
        abs(nums[j + 1])) % 10 == 7):
        count += 1
print(count)
