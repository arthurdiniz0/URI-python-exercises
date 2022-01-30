def main():
    N = int(input())
    for i in range(N):
        soma = 0
        num = int(input())
        for c in range(1, num):
            if num % c == 0:
                soma += c
        if soma == num:
            print('{} eh perfeito'.format(num))
        else:
            print('{} nao eh perfeito'.format(num))

main()