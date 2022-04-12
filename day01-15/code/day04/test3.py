high = 5

for i in range(1, high + 1):
    for j in range(0, i):
        print('*', end='')
    print('')

for i in range(1, high + 1):
    for j in range(0, high - i):
        print(' ', end='')
    for j in range(0, i):
        print('*', end='')
    print('')

for i in range(1, high + 1):
    for j in range(0, high - i):
        print(' ', end='')
    for j in range(0, i):
        print('*', end='')
    for j in range(0, i - 1):
        print('*', end='')
    print('')