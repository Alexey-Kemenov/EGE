nums = [0] * 1000000
ans = 0
for num in range(1, 1000):
    b = bin(num)[2:]
    a = bin(num % 4)[2:]
    b += a
    r = int(b, 2)
    nums[r] = 1
for i in range(1000000 - 65):
    ans = max(ans, sum(nums[i:i + 65]))
print(ans)
