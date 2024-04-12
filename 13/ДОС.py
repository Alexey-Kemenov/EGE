count = 0
for i in range(30):
    ip = f'105.224.200.{224 + i}'
    bin_ip = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
    if bin_ip.count('1') % 4 == 0:
        count += 1
print(count)