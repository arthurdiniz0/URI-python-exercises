a, b, c = input().split()

a1 = int(a)
b1 = int(b)
c1 = int(c)

maiorab = int((a1+b1+abs(a1-b1))/2)
maior = int((maiorab+c1+abs(maiorab-c1))/2)

print('{} eh o maior'.format(maior))