t=int(input())
while t:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    ar.sort()
    ar=ar[::-1]
    sum=0
    z=0
    for i in range(n):
        sum+=max(ar[i]-z,0)
        z+=1
    print(sum%1000000007)

