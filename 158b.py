n=int(input())
ar=list(map(int,input().split()))
d={}
d[1]=0
d[2]=0
d[3]=0
d[4]=0

for i in ar:
    d[i]+=1

total=d[1]//4
left_1=d[1]-total*4

total+=d[2]//2
if d[2]%2==0:
    left_2=0
else:
    left_2=1

if d[3]>=left_1:
    total+=max(d[3],left_1)
    left_1=0
else:
    total+=d[3]
    left_1-=d[3]

if left_1>0 and left_1<=2:
    left_2=0

total+=left_2
print(total+d[4])
