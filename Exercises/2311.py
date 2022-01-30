N = int(input())

for i in range(N):
    nome = input()
    dif = float(input())
    n1, n2, n3, n4, n5, n6, n7 = map(float, input().split())

    maior = max(n1, n2, n3, n4, n5, n6, n7)
    menor = min(n1, n2, n3, n4, n5, n6, n7)

    parcial = n1 + n2 + n3 + n4 + n5 + n6 + n7 - maior - menor

    nota = parcial * dif

    print('{} {:.2f}'.format(nome, nota))