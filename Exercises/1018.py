v = int(input())

nota100 = (v//100)
resto100 = v % 100
nota50 = (resto100//50)
resto50 = resto100 % 50
nota20 = (resto50//20)
resto20 = resto50 % 20
nota10 = (resto20//10)
resto10 = resto20 % 10
nota5 = (resto10//5)
resto5 = resto10 % 5
nota2 = (resto5//2)
resto2 = resto5 % 2
nota1 = (resto2//1)

print(v)
print('{} nota(s) de R$ 100,00'.format(nota100))
print('{} nota(s) de R$ 50,00'.format(nota50))
print('{} nota(s) de R$ 20,00'.format(nota20))
print('{} nota(s) de R$ 10,00'.format(nota10))
print('{} nota(s) de R$ 5,00'.format(nota5))
print('{} nota(s) de R$ 2,00'.format(nota2))
print('{} nota(s) de R$ 1,00'.format(nota1))
