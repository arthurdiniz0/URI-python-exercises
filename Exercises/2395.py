def main():
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())

    largura = int(x/a)
    profundidade = int(y/b)
    altura = int(z/c)

    total = largura*profundidade*altura
    print(total)

main()