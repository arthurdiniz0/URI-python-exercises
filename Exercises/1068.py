def main():
    while True:
        try:
            expressao = input()
            aux = 0
            for c in expressao:
                if c == '(':
                     aux += 1
                if c == ')':
                    aux -= 1
                if aux < 0:
                    break
            if aux != 0:
                print('incorrect')
            else:
                print('correct')
        except EOFError:
            break

main()