class points:
    def __init__(self,a,b,c):
        self.begin=a
        self.end=b
        self.index=c

xxx=int(input())
for t in range(xxx):
    print('Case #',t+1,': ',end='',sep='')
    t-=1
    n=int(input())
    e1=0
    e2=0
    flag=0
    ar=[None]*n
   
    l=[]
    for i in range(n):
        a,b=map(int,input().split())
        l.append(points(a,b,i))

    l=sorted(l, key=lambda obj: obj.begin)
    
    for i in range(n):
        a=l[i].begin
        b=l[i].end
        ind=l[i].index
        # print(ind)
        # print(a,b)
        
        if a>=e1:
            e1=b
            # print('C',end='')
            ar[ind]='C'
        elif a>=e2:
            e2=b
            # print('J',end='')
            ar[ind]='J'
        else:
            flag=1
            
    if flag==1:
        print('IMPOSSIBLE',end='')
    else:
        for i in ar:
            print(i,end='')
    print()
