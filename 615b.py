t=int(input())
while t:
    t-=1
    n=int(input())
    d={}
    
    for i in range(n):
        a,b=map(int,input().split())
        d[a]=b
    way=[] 
    key=sorted(d)
    curr=0
    curry=0
    print(key)
    for i in key:
        iter=i-curr
        if iter!=0:
            for j in range(curr,i):
                way.append(1)
            curr=i
            curry=d[i]
        else:
            for j in range(curry,d[i]):
                way.append(0)
            curry=d[i]
            curr=i
    for i in way:
        if i:
            print('R',end='')
        else:
            print('U',end='')
