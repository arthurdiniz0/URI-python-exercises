def main():
    N = int(input())
    seq = input().split()
    minposs = 1
    i = 0
    while i < N:
        try:
            r_atual = int(seq[i+1]) - int(seq[i])
            prox_r = int(seq[i+2]) - int(seq[i+1])
            if r_atual != prox_r:
                minposs += 1
                i += 2
            else:
                i += 1
        except:
            break
    print(minposs)



main()