t=int(input())
while t:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    flag=0
    
    if n>=3:
        for i in range(n):
            for j in range(i+2,n):
                if ar[i]==ar[j]:
                    flag=1
                    break
    print("YES" if flag==1 else "NO")
