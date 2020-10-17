s=input()
m=int(input())
hs=[]
dot=[]
for i in range(len(s)):
    if s[i]=='.':
        dot.append(i)
    else:
        hs.append(i)

for i in range(m):
    cnt=0
    l,r=map(int,input().split())
    
    for j in dot:
        if j+l-1 in dot:
            cnt+=1

    for j in hs:
        if j+l-1 in hs:
            cnt+=1
    
    
    print(cnt)
