s=input()
flag=0
cnt=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        cnt+=1
    else:
        cnt=0
    if cnt==6:
        flag=1
        break
if flag==1:
    print('YES')
else:
    print('NO')

