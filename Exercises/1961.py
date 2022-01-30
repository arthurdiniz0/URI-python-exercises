p, n = map(int, input().split())
lista = input().split()
altatual = int(lista[0])
for i in range(n):

    altprox = int(lista[i])
    if altprox - altatual > p or altprox - altatual < -p:
        win = False
        break
    else:
        win = True
        altatual = altprox

if win:
    print('YOU WIN')
else:
    print('GAME OVER')


