def main():
    n = int(input())
    total = 0
    ratos = 0
    sapos = 0
    coelhos = 0
    for i in range(n):
        num, animal = input().split()
        num = int(num)
        if animal == 'S':
            sapos += num
            total += num
        elif animal == 'R':
            ratos += num
            total += num
        elif animal == 'C':
            coelhos += num
            total += num

    print('Total: {} cobaias'.format(total))
    print('Total de coelhos: {}'.format(coelhos))
    print('Total de ratos: {}'.format(ratos))
    print('Total de sapos: {}'.format(sapos))
    print('Percentual de coelhos: {:.2f} %'.format(coelhos/total*100))
    print('Percentual de ratos: {:.2f} %'.format(ratos/total*100))
    print('Percentual de sapos: {:.2f} %'.format(sapos/total*100))

main()