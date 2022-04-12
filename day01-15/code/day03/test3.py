a = float(input('第一条边：'))
b = float(input('第二条边：'))
c = float(input('第三条边：'))
tmp = 0.0

if a > b:
    tmp = a
    a = b
    b = tmp
elif a > c:
    tmp = a
    a = c
    c = tmp
elif b > c:
    tmp = b
    b = c
    c = tmp

if a + b > c:   # a + b > c and a + c > b and b + c > a
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    z = a + b + c
    print('周长 = %.2f\n面积 = %.2f' % (z, p))
else:
    print('无法构成三角形')
