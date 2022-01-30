def main():
    N = int(input())
    for i in range(0, N):
        x, y = map(int, input().split())
        impares = 0
        if x < y:
            if abs(x - y) > abs(1):
                for c in range(x + 1, y):
                    if c % 2 != 0:
                        impares += c
                print(impares)
            else:
                print(0)
        elif x > y:
            if abs(x - y) > abs(1):
                for c in range(x - 1, y, -1):
                    if c % 2 != 0:
                        impares += c
                print(impares)
            else:
                print(0)
        else:
            print(0)
main()