t=int(input())
while t:
    flag=0
    d={}
    e={}
    t-=1
    s=input()
    n=len(s)

    for i in range(n//2):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1

    for i in range(n//2,n):
        if s[i] in e:
            e[s[i]]+=1
        else:
            e[s[i]]=1

    if len(d)==len(e):
        for i in d:
            if i not in e or d[i]!=e[i]:
                flag=1
                break
    else:
t=int(input())
while t:
    flag=0
    d={}
    e={}
    t-=1
    s=input()
    n=len(s)

    for i in range(n//2):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1

    for i in range(n//2,n):
        if s[i] in e:
            e[s[i]]+=1
        else:
            e[s[i]]=1

    if len(d)==len(e):
        for i in d:
            if i not in e or d[i]!=e[i]:
                flag=1
                break
    else:
        flag=1

    print('YES' if flag==0 else 'NO')
        flag=1

    print('YES' if flag==0 else 'NO')
