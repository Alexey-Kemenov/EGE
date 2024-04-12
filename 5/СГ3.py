s = set()
count = 0
for i in range(1_000_000_000, 9_999_999_999):
    count += len(set(str(i)))
print(count)