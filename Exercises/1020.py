dinput = int(input())

anos = dinput//365
restoanos = dinput % 365
meses = restoanos//30
dias = restoanos % 30

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos, meses, dias))
