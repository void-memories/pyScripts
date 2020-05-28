t=int(input())
while t:
    flag=0
    t-=1
    x,y,k,n=map(int,input().split())
    for i in range(n):
        p,c=map(int,input().split())
        if p+y>=x and c<=k:
            print('LuckyChef')
            flag=1
            break
    if flag==0:
        print('UnluckyChef')
