t=int(input())
while t:
    t-=1
    s=input()
    max=-1
    n=len(s)
    ind=[]
    ind.append(0)
    
    for i in range(n):
        if s[i]=='R':
            ind.append(i+1)

    ind.append(n+1)

    for i in range(len(ind)-1):
        if ind[i+1]-ind[i]>max:
            max=ind[i+1]-ind[i]
    print(max)

