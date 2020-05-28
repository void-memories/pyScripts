t=int(input())
while t:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    br=[]
    dr=[0]*(n+1)
    count=1
    count2=0
    cr=[0]*(n+1)
    for i in range(n):
        br[i+1]=ar[i]
    while count2<n-1:
        for j in range(1,n+1):
            cr[j]=br[br[j]]
            if cr[j]==j:
                dr[j]=count
                count2+=1
        count+=1
                

    