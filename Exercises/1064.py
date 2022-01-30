def main():
    positivos = 0
    soma = 0
    for n in range(6):
        num = float(input())
        if num > 0:
            positivos += 1
            soma += num

    print('{} valores positivos'.format(positivos))
    print('{:.1f}'.format(soma/positivos))

main()