def main():
    a0, b0, c0 = map(float, input().split())

    if a0 >= b0 >= c0:
        a, b, c = a0, b0, c0
    elif a0 >= c0 >= b0:
        a, b, c = a0, c0, b0
    elif b0 >= a0 >= c0:
        a, b, c = b0, a0, c0
    elif b0 >= c0 >= a0:
        a, b, c = b0, c0, a0
    elif c0 >= a0 >= b0:
        a, b, c = c0, a0, b0
    elif c0 >= b0 >= a0:
        a, b, c = c0, b0, a0


    if a >= b + c:
        print('Invalido')
    else:
        if a == b != c or a == c != b or b == c != a:
            print('Valido-Isoceles')
        elif: if a == b == c:
            print('Valido-Equilatero')
        else:
            print('Valido-Escaleno')
        if a ** 2 == b ** 2 + c ** 2:
            print('Retangulo: S')
        else:
            print('Retangulo: N')


main()