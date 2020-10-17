size,n=map(int,input().split())
cnt=0
for i in range(1,size+1):
    if n%i==0 and n//i<=size:
        cnt+=1
print(cnt)

