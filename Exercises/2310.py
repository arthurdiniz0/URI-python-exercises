N = int(input())
totalts = 0
totaltb = 0
totalta = 0
totals = 0
totalb = 0
totala = 0
for i in range(N):
    nome = input()
    ts, tb, ta = map(int, input().split())
    s, b, a = map(int, input().split())

    totalts += ts
    totaltb += tb
    totalta += ta
    totals += s
    totalb += b
    totala += a



print('Pontos de Saque: {:.2f} %.'.format((totals/totalts)*100))
print('Pontos de Bloqueio: {:.2f} %.'.format((totalb/totaltb)*100))
print('Pontos de Ataque: {:.2f} %.'.format((totala/totalta)*100))
