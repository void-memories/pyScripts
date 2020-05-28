n=int(input())
s=input()
cnt=0

for i in range(n):
    if i==0:
        temp=s[i]
    else:
        if s[i]==temp:
            cnt+=1
        else:
            temp=s[i]
print(cnt)
