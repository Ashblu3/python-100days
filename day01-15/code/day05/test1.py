a = 0
b = 1
print('0 1 ', end='')

for i in range(0, 18):
    c = a + b
    print('%d ' % (c), end='')
    a = b
    b = c

