def main():
    x, y = map(int, input().split())
    while True:
        if x > 0 and y > 0:
            print('primeiro')
            x, y = map(int, input().split())
        elif x < 0 and y > 0:
            print('segundo')
            x, y = map(int, input().split())
        elif x < 0 and y < 0:
            print('terceiro')
            x, y = map(int, input().split())
        elif x > 0 and y < 0:
            print('quarto')
            x, y = map(int, input().split())
        else:
            quit()
main()