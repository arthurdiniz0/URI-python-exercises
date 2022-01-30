hi, mi, hf, mf = map(int, input().split())

durou = (hf*60 + mf) - (hi*60 + mi)
horas = 0
if durou <= 0:
    horas += 24
horas += durou // 60
minutos = durou % 60
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))