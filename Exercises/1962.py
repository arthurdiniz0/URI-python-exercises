N = int(input())
for i in range(N):
    anosp = int(input())
    if anosp < 2015:
        print('{} D.C.'.format(2015 - anosp))
    elif anosp >= 2015:
        ac = -(2015 - anosp)
        print('{} A.C.'.format(ac+1))