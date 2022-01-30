def main():
    N = int(input())
    for i in range(N):
        num = int(input())
        if num == 2:
            print('2 eh primo')
        for c in range(2, num):
            if num % c == 0:
                print('{} nao eh primo'.format(num))
                break
            if c == num - 1:
                print('{} eh primo'.format(num))

main()
