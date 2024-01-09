ip = '119.167.50.77'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
ip = '119.167.48.0'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))