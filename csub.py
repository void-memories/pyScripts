t=int(input())
while t:
    cnt=0
    t-=1
    n=int(input())
    s=input()
    for i in s:
        if i=='1':
            cnt+=1
    print(cnt*(cnt+1)//2)
