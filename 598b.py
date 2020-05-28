def check(ar):
    for i in range(1,len(ar)):
        if ar[i]==0:
            return 1
    return 0
    
t=int(input())
while t:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))

    visited=[0]*(n+1)
    visit=[]
    
    for i in range(n):
        visit.append(i+1)
    
    prev=[]
    q=0
    while(prev!=ar):
        q+=1
        prev=ar.copy()
        
        z=0
        while(z<n):
            #print(2)
            e=visit[z]
            for i in range(n):
                if ar[i]==e and i!=0 and visited[i]==0 and ar[i-1]>ar[i]:
                    temp=ar[i-1]
                    ar[i-1]=ar[i]
                    ar[i]=temp
                    visited[i]=1
                    z=-1
            z+=1
                    
            #print(ar)
        
    for i in ar:
        print(i,end=' ')
    print()

