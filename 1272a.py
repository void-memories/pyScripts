def dist(a,b,c):
    return abs(a-b)+abs(b-c)+abs(c-a)
q=int(input())
while q:
    q-=1
    ar=list(map(int,input().split()))
    ar.sort()
    if ar[0]==ar[1]==ar[2]:
        print(0)
    elif ar[0]==ar[1]:
        print(dist(ar[0],ar[0],ar[2]-1))
    elif ar[1]==ar[2]:
        print(dist(ar[0]+1,ar[1],ar[2]))
