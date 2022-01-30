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
        print('NAO FORMA TRIANGULO')
    else:
        if a ** 2 == b ** 2 + c ** 2:
            print('TRIANGULO RETANGULO')
        if a ** 2 > b ** 2 + c ** 2:
            print('TRIANGULO OBTUSANGULO')
        if a ** 2 < b ** 2 + c ** 2:
            print('TRIANGULO ACUTANGULO')
        if a == b == c:
            print('TRIANGULO EQUILATERO')
        if a == b != c or a == c != b or b == c != a:
            print('TRIANGULO ISOSCELES')


main()