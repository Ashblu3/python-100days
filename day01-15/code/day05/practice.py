import math

# # 水仙花
# def find(num):
#     tmp = num
#     sum = 0
#     while tmp:
#         a = tmp % 10
#         tmp = tmp // 10
#         sum += math.pow(a, 3)
#     return num == sum

# for num in range(100, 1000):
#     if find(num):
#         print('%d是水仙花数' % (num))


# # 百鸡百钱
# for x in range(0, 101):             # 公鸡的数量
#     for y in range(0, 101 - x):     # 母鸡的数量
#         z = 100 - x - y
#         if z % 3 != 0:
#             continue
#         if x * 5 + y * 3 + z / 3 == 100:
#             print('公鸡%d只，母鸡%d只，小鸡%d只' % (x, y, z))
