k,n,w=map(int,input().split())
total=(w*(w+1)//2)*k
res=total-n
if res<=0:
    print(0)
else:
    print(res)
