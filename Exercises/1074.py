def main():
    N = int(input())
    for i in range(0, N):
        num = int(input())
        if num > 0:
            if num % 2 == 0:
                print('ODD POSITIVE')
            else:
                print('EVEN POSITIVE')
        elif num < 0:
            if num % 2 == 0:
                print('ODD NEGATIVE')
            else:
                print('EVEN NEGATIVE')
        else:
            print('NULL')

main()