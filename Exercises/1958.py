num = input()

if num[0] == '-':
    sinal = '-'
    num = float(num[1:])
else:
    sinal = '+'
    num = float(num)

print('{}{:.4E}'.format(sinal, num))

