from math import pow


def is_palindrome(num):
    l = 1
    flag = True
    while num // pow(10, l):
        l += 1
    for i in range(1, l // 2 + 1):
        x = num % pow(10, i) // pow(10, i -1)   # 末尾对比的数
        y = num // pow(10, l - i) % 10          # 首部对比的数
        if x != y:
            flag = False
            break
    return flag

num = int(input('num = '))
if is_palindrome(num):
    print('%d is palindrome' % num)
else:
    print('%d isn\'t palindrome' % num)
    