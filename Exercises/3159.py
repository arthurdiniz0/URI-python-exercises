def main():
    n = int(input())

    num2 = ['a', 'b', 'c']
    num3 = ['d', 'e', 'f']
    num4 = ['g', 'h', 'i']
    num5 = ['j', 'k', 'l']
    num6 = ['m', 'n', 'o']
    num7 = ['p', 'q', 'r', 's']
    num8 = ['t', 'u', 'v']
    num9 = ['w', 'x', 'y', 'z']

    for i in range(n):
        txt = input()
        num_ant = 0
        for caracter in range(len(txt)):
            #espaço

            if txt[caracter] == ' ':
                print(0, end='')
                num_ant = 0
            #letra maiscula
            upper = False
            if txt[caracter].isupper():
                upper = True

            #num2
            if txt[caracter].lower() in num2:
                if upper:
                    print('#', end='')
                elif num_ant == 2:
                    print('*', end='')
                for a in range(num2.index(txt[caracter].lower()) + 1):
                    print('2', end='')
                num_ant = 2
            #num3
            elif txt[caracter].lower() in num3:
                if upper:
                    print('#', end='')
                elif num_ant == 3:
                    print('*', end='')
                for a in range(num3.index(txt[caracter].lower()) + 1):
                    print('3', end='')
                num_ant = 3
            #num4
            elif txt[caracter].lower() in num4:
                if upper:
                    print('#', end='')
                elif num_ant == 4:
                    print('*', end='')
                for a in range(num4.index(txt[caracter].lower()) + 1):
                    print('4', end='')
                num_ant = 4
            #num5
            elif txt[caracter].lower() in num5:
                if upper:
                    print('#', end='')
                elif num_ant == 5:
                    print('*', end='')
                for a in range(num5.index(txt[caracter].lower()) + 1):
                    print('5', end='')
                num_ant = 5
            #num6
            elif txt[caracter].lower() in num6:
                if upper:
                    print('#', end='')
                elif num_ant == 6:
                    print('*', end='')
                for a in range(num6.index(txt[caracter].lower()) + 1):
                    print('6', end='')
                num_ant = 6
            #num7
            elif txt[caracter].lower() in num7:
                if upper:
                    print('#', end='')
                elif num_ant == 7:
                    print('*', end='')
                for a in range(num7.index(txt[caracter].lower()) + 1):
                    print('7', end='')
                num_ant = 7
            #num8
            elif txt[caracter].lower() in num8:
                if upper:
                    print('#', end='')
                elif num_ant == 8:
                    print('*', end='')
                for a in range(num8.index(txt[caracter].lower()) + 1):
                    print('8', end='')
                num_ant = 8
            #num9
            elif txt[caracter].lower() in num9:
                if upper:
                    print('#', end='')
                elif num_ant == 9:
                    print('*', end='')
                for a in range(num9.index(txt[caracter].lower()) + 1):
                    print('9', end='')
                num_ant = 9
        print('')

main()