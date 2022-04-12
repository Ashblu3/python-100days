value = float(input('请输入长度: '))
unit = input('请输入单位: ')

if unit == 'cm' or unit == 'in':
    if unit == 'cm':        # 没必要的嵌套
        cm = value
        inch =  cm / 2.54
    else:
        inch = value
        cm = inch * 2.54
    print('%.2lfin = %.2lfcm' % (inch, cm))
else:
    print('请输入正确的单位')

