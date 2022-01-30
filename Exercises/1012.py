a, b, c = input().split()

a1, b1, c1 = float(a), float(b), float(c)

print('TRIANGULO: {:.3f}'.format((a1*c1)/2))
print('CIRCULO: {:.3f}'.format(3.14159*c1*c1))
print('TRAPEZIO: {:.3f}'.format(((a1+b1)*c1)/2))
print('QUADRADO: {:.3f}'.format(b1*b1))
print('RETANGULO: {:.3f}'.format(a1*b1))

print("""TRIANGULO: {:.3f""")