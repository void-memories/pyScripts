t=int(input())
while t:
    cnt=0
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    ind=[]
    
    for i in range(n):
        ar[i]=abs(ar[i])%4
        if (ar[i])==2:
            ind.append([2,i])
        elif (ar[i])==0:
            ind.append([0,i])
    # print(ind)
    for i in range(len(ind)):
        if len(ind)>1:
            if i==0 and ind[i][0]==2:
                cnt+=(ind[i+1][1]-ind[i][1])*(ind[i][1]+1)
                # print(cnt,'1')
            elif i==len(ind)-1 and ind[i][0]==2:
                cnt+=(ind[i][1]-ind[i-1][1])*(n-ind[i][1])
                # print(cnt,'2')
            elif ind[i][0]==2:
                cnt+=(ind[i][1]-ind[i-1][1])*(ind[i+1][1]-ind[i][1])
                # print(cnt,'3')
        elif len(ind)==1 and ind[0][0]==2:
            cnt+=(ind[i][1]+1)*(n-ind[i][1])
            # print(cnt,'4')
    

    print((n*(n+1)//2)-cnt)
    
    # cnt=0
    # for i in range(n):
    #     prod=1
    #     for j in range(i,n):
    #         prod*=ar[j]
    #         if prod%4!=2:
    #             cnt+=1
    # print(cnt)