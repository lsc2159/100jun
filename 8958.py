N=int(input())
for i in range(N):
    score=0
    plus=0

    OX=input()
    for x in range(len(OX)):
        if OX[x]=='O':
            plus+=1
            score+=plus
        else:
            plus=0
    print(score)