N=int(input('N 숫자 입력: '))
if 1<=N<=100:
    print(N)
    a=input()
    sum=0
    for i in range(N):
        sum+=int(a[i])
    print(sum)


