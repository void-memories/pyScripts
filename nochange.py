t=int(input())
while t:
    t-=1
    n,p=input().split()
    n,p=int(n),int(p)
    l=list(map(int,input().split()))

    flag=0

    for i in range(n):
        if p%l[i]!=0:
            flag=1
            dc=i
            break
    
    if flag==0:
        print("NO")
    else:
        q=p//l[dc]
        q+=1

        print("YES ",end="")
        for i in range(n):
            if i==dc:
                print(q,sep=" ",end="")
            else:
                print(0,sep=" ",end="")