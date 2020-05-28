def check(a, b):
    x= max(0, min(a[1], b[1]) - max(a[0], b[0])+1)
    return x
t=int(input())
while t:
    t-=1
    x=[]
    y=[]
    n=int(input())
    count=[0]*n
    
    for i in range(n):
        a,b=input().split()
        x.append(a)
        y.append(b)
        
        if i>0:
            for j in range(i):
                if check([int(a),int(b)],[int(x[j]),int(y[j])]):
                    count[i]+=1
                    count[j]+=1
    count.sort()
    
    
    if count[0]==0:
        print(0)
    elif n-count[0] >= 2:
        print(count[0])
    else:
        print(-1)
                    
    
    
    #print(count)
            
        