def main():
    nada, dia_i = input().split()
    dia_i = int(dia_i)
    h1, m1, s1 = map(int, input().split(" : "))
    nada, dia_f = input().split()
    dia_f = int(dia_f)
    h2, m2, s2 = map(int, input().split(" : "))

    segundos2 = s2 + m2*60 + h2*3600 + dia_f*86400
    segundos1 = s1 + m1*60 + h1*3600 + dia_i*86400

    tempo = segundos2 - segundos1
    dias = tempo // 86400
    tempo = tempo % 86400
    horas = tempo // 3600
    tempo = tempo % 3600
    minutos = tempo // 60
    segundos = tempo % 60

    print('{} dia(s)'.format(dias))
    print('{} hora(s)'.format(horas))
    print('{} minuto(s)'.format(minutos))
    print('{} segundo(s)'.format(segundos))

main()