n=int(input())
total=max=0
for i in range(n):
    a,b=map(int,input().split())
    total=total+(b-a)
    if total>max:
        max=total
print(max)
