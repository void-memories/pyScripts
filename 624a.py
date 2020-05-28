t=int(input())
while t:
    t-=1
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif a<b:
        if (b-a)%2==0:
            print(2)
        else:
            print(1)
    else:
        if (a-b)%2==0:
            print(1)
        else:
            print(2)

