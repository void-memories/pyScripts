t=int(input())
while t:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))

    for i in range(n):
        if i==0:
            sum=ar[i]+ar[i+1]+ar[n-1]
        elif i==n-1:
            sum=ar[i]+ar[i-1]+ar[0]
        else:
            sum=ar[i]+ar[i+1]+ar[i-1]
        
        if sum>max:
                max=sum


