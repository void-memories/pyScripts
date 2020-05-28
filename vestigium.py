t=int(input())
while t:
    t-=1
    n=int(input())
    mat=[]
    sum=0
    col=0
    row=0
    for i in range(n):
        ar=list(map(int,input().split()))
        mat.append(ar)
    
    for i in range(n):
        if len(set(mat[i]))<n:
            row+=1
        sum=mat[i][i]

    for i in range(n):
        c=set()
        for j in range(n):
            c.add(mat[j][i])
        if len(c)<n:
            col+=1