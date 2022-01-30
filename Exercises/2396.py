def main():
    carros, voltas = map(int, input().split())
    tempos = []
    for n in range(1, carros+1):

        tstrings = input().split()
        tsoma = 0
        for c in tstrings:
            tsoma += int(c)

        tempos.append(tsoma)

    tempos_aux = sorted(tempos)

    val1 = tempos_aux[0]
    val2 = tempos_aux[1]
    val3 = tempos_aux[2]

    primeiro = tempos.index(val1) + 1
    segundo = tempos.index(val2) + 1
    terceiro = tempos.index(val3) + 1


    print(primeiro)
    print(segundo)
    print(terceiro)


main()