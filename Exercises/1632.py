def main():
    N = int(input())
    for i in range(N):
        comb = 1
        senha = input().lower()
        for c in senha:
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='s':
                comb *= 3
            else:
                comb *=2
        print(comb)
main()
