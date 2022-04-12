for x in range(2, 100):
    flag = 1
    for i in range(2, x):
        if x % i == 0:
            flag = 0
            break
    if flag:
        print('%d ' % (x), end='')