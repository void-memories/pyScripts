n=int(input())
l=list(map(int,input().split()))
count=0
max=-1

for i in range(n-1):
    if l[i]<l[i+1]:
        count+=1
    else:
        if count>max:
            max=count
        count=0
    if i==n-2:
        if count>max:
            max=count
        count=0
if max==0:
    print(0)
else:
    print(max+1)