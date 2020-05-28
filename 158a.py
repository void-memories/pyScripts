n,k=map(int,input().split())
ar=list(map(int,input().split()))
margin=ar[k-1]
cnt=0
for i in ar:
    if i>=margin and i>0:
        cnt+=1
print(cnt)
