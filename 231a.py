n=int(input())
cnt=0
for i in range(n):
    ar=list(map(int,input().split()))
    if sum(ar)>1:
        cnt+=1
print(cnt)
