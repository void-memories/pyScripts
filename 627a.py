t=int(input())
while t:
    t-=1
    flag=0
    n=int(input())
    ar=list(map(int,input().split()))

    for i in range(n):
        for j in range(i,n):
            if abs(ar[i]-ar[j])%2!=0:
                flag=1
                break
    if flag==1:
        print('NO')
    else:
        print('YES')

