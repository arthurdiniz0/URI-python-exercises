svalor = int(input())

h = svalor//3600
hsobra = svalor % 3600
m = hsobra//60
s = hsobra % 60

print('{}:{}:{}'.format(h, m, s))
