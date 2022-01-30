def main():
    areatotal = [[0 for y in range(101)] for x in range(101)]

    N = int(input())

    for i in range(N):
        xi, xf, yi, yf = map(int, input().split())
        for l in range(xi + 1, xf + 1):
            for c in range(yi + 1, yf + 1):
                areatotal[l][c] = 1
    areaocupada = 0
    for ponto in areatotal:
        areaocupada += sum(ponto)

    print(areaocupada)

main()

