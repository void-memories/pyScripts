t=int(input())
while t:
    t-=1
    a,b,c,x=map(int,input().split())

    m=max(a,b,c)
    req=m-a+m-b+m-c
    if req>x or (x-req)%3!=0:
        print('NO')
    else:
        print('YES')
