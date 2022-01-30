a, b, c = input().split()
d, e, f = input().split()

b1, c1, e1, f1 = int(b), float(c), int(e), float(f)

print('VALOR A PAGAR: R$ {:.2f}'.format(b1*c1 + e1*f1))
