import math
def Sieve(n): 
    ar=set()
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
	
    for p in range(2, n): 
	    if prime[p]: 
		    ar.add(p)
    return ar

t=int(input())
while t:
    t-=1
    n=int(input())
    ar=Sieve(n+1)
    ar.add(1)
    p=list(ar)
    sq=[]
    extra=[]

    last=1
    z=0
    while last<=n:
        if last!=1:
            sq.append(last)
            ar.add(last)
        last=p[z]*p[z]
            
        
        z+=1

    
    for i in range(1,n):
        if i not in ar:
            extra.append(i)
    
    cnt=len(extra)+1
    if len(sq)>0:
        cnt+=1
    
    print(cnt)
    print(len(p),end=' ')
    for i in p:
        print(i,end=' ')
    print()

    if len(sq)!=0:
        print(len(sq),end=' ')
        for i in sq:
            print(i,end=' ')
        print()

    if len(extra)!=0:
        for i in extra:
            print(i)

        





