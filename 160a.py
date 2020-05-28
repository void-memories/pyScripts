n=int(input())
ar=list(map(int,input().split()))
total=sum(ar)
ar.sort(reverse=True)
count=0
curr=0
for i in ar:
    curr+=i
    count+=1
    if curr>total-curr:
        break
print(count)

