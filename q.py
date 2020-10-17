a,b,c,d=map(int,input().split())
way=[[4+a+2,'X A F L M Y'],
[3+b+2,'X E G M Y'],
[4+4+d,'X B D H J K Y'],
[4+3+c,'X B D H I Y']]

index=0
mini=float('inf')
for i in range(4):
    if way[i][0]<mini:
        mini=way[i][0]
        index=way[i][1]
    # print(way[i][0],way[i][1])

minLen=float('inf')
for i in range(4):
    if mini==way[i][0]:
        if len(way[i][1])<minLen:
            ans=way[i][1]
            minLen=len(way[i][1])
print(ans)