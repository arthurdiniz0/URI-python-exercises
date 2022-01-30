def main():
    N = int(input())
    for i in range(N):
        inicio, fim = map(int, input().split())
        for c in range(inicio, fim+1):
            print(c, end='')
        for b in reversed(range(inicio, fim+1)):
            if 0 <= b < 10:
                num = str(b)
            elif b >= 10:
                num = ''.join(reversed(str(b)))
            print(num, end='')
        print('')
main()