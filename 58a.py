s=input()
flag=0
test=['h','e','l','l','o']
for i in range(len(s)):
    z=0
    for j in range(i,len(s)): 
        if s[j]==test[z]:
            z+=1
            if z==5:
                flag=1
                break
    if flag==1:
        break
if flag==1:
    print('YES')
else:
    print('NO')
