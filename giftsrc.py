t=int(input())
while t:
    t-=1
    n=int(input())
    s=input()
    x=0
    y=0

    for i in range(n):
        if i==0:
            if s[i]=='L':
                x-=1
            elif s[i]=='R':
                x+=1
            elif s[i]=='U':
                y+=1
            elif s[i]=='D':
                y-=1
        if s[i]!=s[i-1] and i!=0 and not(s[i]=='R' and s[i-1]=='L') and not(s[i]=='L' and s[i-1]=='R') and not(s[i]=='U' and s[i-1]=='D') and not(s[i]=='D' and s[i-1]=='U'):
            if s[i]=='L':
                x-=1
            elif s[i]=='R':
                x+=1
            elif s[i]=='U':
                y+=1
            elif s[i]=='D':
                y-=1
    
    print(x,y)

