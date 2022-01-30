def main():
    while True:
        soma = 0
        m, n = map(int, input().split())
        if m <= 0 or n <= 0:
            break
        else:
            if m > n:
                maior = m
                menor = n
            elif n > m:
                maior = n
                menor = m
            for c in range(menor, maior + 1):
                print(c, end=' ')
                soma += c
            print('Sum={}'.format(soma))


main()

