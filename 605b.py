n,k=map(int,input().split())
sum=0
cnt=0
d={}
s=input()
ar=list(map(str,input().split()))
ar=set(ar)

uw=[]
for i in range(len(s)):
    if s[i] in ar:
        uw.append(i)
#print(uw)

for i in range(len(uw)):
    if i==0:
        start=0
        end=0
        streak=1
        if i==len(uw)-1:
            sum+=(end-start+1)*(end-start+2)//2
    else:
        if uw[start]+streak==uw[i]:
            end=i
            streak+=1
            if i==len(uw)-1:
                sum+=(end-start+1)*(end-start+2)//2
        else:
            sum+=(end-start+1)*(end-start+2)//2
            start=i
            end=i
            streak=1
            if i==len(uw)-1:
                sum+=(end-start+1)*(end-start+2)//2
            
            
    #print(start,end)
print(sum)


