import datetime

d2, m2 = map(int, input().split())
d1, m1 = map(int, input().split())

data2 = datetime.datetime.strptime(f'2001-{m2}-{d2}', '%Y-%m-%d')
data1 = datetime.datetime.strptime(f'2001-{m1}-{d1}', '%Y-%m-%d')

dias = abs((data2 - data1).days)

print(dias)