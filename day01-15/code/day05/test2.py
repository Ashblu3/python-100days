for x in range(1, 10000):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    if sum == x:
        print('%d是完美数' % (x))
