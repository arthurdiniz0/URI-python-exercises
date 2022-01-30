def main():
    maior = 0
    for n in range(100):
        val = int(input())
        if val > maior:
            maior = val
            pos = n + 1
    print(maior)
    print(pos)
main()

