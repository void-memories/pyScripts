t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    ar=input()
    dist=[]
    cnt=0

    for i in range(len(ar)):
        
        if ar[i]==1:
            if start!=-1:
                dist.append(i-start)
                start=-1


    if start!=-1 and ar[len(ar)-1]==0:
        dist.append(len(ar)-1-start)

    s=0

    for i in dist:
        s+=max(i-2,0)

    print(s)

        
        