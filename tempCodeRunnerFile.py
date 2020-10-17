t=int(input())
while t:
    t-=1
    n,p=map(int,input().split())

    b=[]
    for i in range(1,61):
        a=[]
        for j in range(1,61):
            print(1,i,j,i,j)
            temp=int(input())
            a.append(temp)
        b.append(a)

    print(2)
    for i in range(60):
        for j in range(60):
            print(b[i][j],sep==' ')
        print()
