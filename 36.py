l = float(input('长'))
k = float(input('宽'))
if l < 0 or k < 0:
    print('invalid input')
else:
    print('周长：' + str(2*(l+k)))
    print('面积：' + str((l*k)))
