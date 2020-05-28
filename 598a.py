t=int(input())
while t:
    t-=1
    a,b,n,s=map(int,input().split())
    if s<=b:
        print('yes')
    elif a*n<=s and s-a*n<=b:
        print('yes')
    elif a*n>s and s%n<=b:
        print('yes')
    else:
        print('no')

