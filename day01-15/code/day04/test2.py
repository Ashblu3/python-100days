a = int(input('a = '))
b = int(input('b = '))
x = 0   # 公约数
y = 0   # 公倍数

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        x = i

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        y = i
        break

print('最大公约数 = %d\n最小公倍数 = %d' % (x, y))

# 从两个数中较小的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break