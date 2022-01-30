def main():
    N = int(input())
    for i in range(N):
        lista = []
        p1, p2 = input().split()

        if len(p1) > len(p2):
            maior = p1
            menor = p2
        else:
            maior = p2
            menor = p1

        palavra = ''

        for c in range(len(menor)):
            palavra = palavra + p1[c]
            palavra = palavra + p2[c]

        palavra = palavra + maior[len(menor):]

        print(palavra)



main()