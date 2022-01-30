def main():
    N = int(input())
    for c in range(N):
        v1, v2, v3 = map(float, input().split())
        print('{:.1f}'.format((v1*2+v2*3+v3*5)/10))
main()