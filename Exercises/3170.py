def main():
    B = int(input())
    G = int(input())

    if G % 2 == 0:
        faltam = int(G / 2 - B)
        if faltam == 0:
            print('Amelia tem todas bolinhas!')
        else:
            print('Faltam {} bolinha(s)'.format(faltam))
    elif G % 2 != 0:
        faltam = int(G / 2 - B - 0.5)
        if faltam == 0:
            print('Amelia tem todas bolinhas!')
        else:
            print('Faltam {} bolinha(s)'.format(faltam))

main()
