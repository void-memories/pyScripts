t=int(input())
while t:
    cnt=0
    t-=1
    n,k=map(int,input().split())
    ar=list(map(int,input().split()))
    for i in ar:
        if (i+k)%7==0:
            cnt+=1
    print(cnt)
