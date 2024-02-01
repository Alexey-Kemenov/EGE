def convert(nums):
    nums = nums[::-1]
    return sum(nums[i] * 40 ** i for i in range(len(nums)))



for x in range(40):
    for y in range(40):
        a = convert([5, 7, x, 6, 9, 2, y, 1, 9])
        if a % 39 == 0:
            b = y * 40 + x
            if int(b ** 0.5) ** 2 == b:
                print(b)
