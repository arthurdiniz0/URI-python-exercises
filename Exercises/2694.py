def main():
    n = int(input())

    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(n):
        string = input()
        so_num = ''
        for c in string:
            if not(c in numeros):
                num = ' '
            else:
                num = c
            so_num += num

        lista = so_num.split(' ')
        soma = 0
        for a in lista:
            if a == '':
                continue
            else:
                soma += int(a)
        print(soma)
main()