import sys
sys.setrecursionlimit(10**6) 

def prim(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" ",flush=True)
        print(flush=True)

    print("\n",flush=True)
def FindMatrix(rows,cols,r,c,m,n,matrix):
    count=0
    if(rows[r]>0 and cols[c]>0):
        matrix[r][c]=1
        rows[r]-=1
        cols[c]-=1
        if(r==m-1) and (cols[c]!=0):
            matrix[r][c]=0
            rows[r]+=1
            cols[c]+=1
            return 0
        if(c==n-1) and(rows[r]!=0):
            matrix[r][c]=0
            rows[r]+=1
            cols[c]+=1
            return 0
        cc=c
        rr=r
        if(cc<n-1):
            cc+=1
        else:
            cc=0
            if(rr<m-1):
                rr+=1
            else:
                prim(matrix)
                matrix[r][c]=0
                rows[r]+=1
                cols[c]+=1
                return 1
        count=FindMatrix(rows,cols,rr,cc,m,n,matrix)
        matrix[r][c]=0
        rows[r]+=1
        cols[c]+=1
        if(r==m-1 or c==n-1):
            return count
    if(r==m-1) and(cols[c]!=0):
        return 0
    if(c==n-1) and(rows[r]!=0):
        return 0
    cc=c
    rr=r
    if(cc<n-1):
        cc+=1
    else:
        cc=0
        if(rr<m-1):
            rr+=1
        else:
            prim(matrix)
            return 1
    return count+FindMatrix(rows,cols,rr,cc,m,n,matrix)


t=int(input())
while t:
    t-=1
    n,p=map(int,input().split())

    rows=[]
    cols=[]
    matrix=[]

    for i in range(60):
        a=[]
        for j in range(60):
            a.append(0)
        matrix.append(a)

    for i in range(1,61):
        print(1,i,1,i,60,flush=True)
        temp=int(input())
        rows.append(temp)

    for i in range(1,61):
        print(1,1,i,60,i,flush=True)
        temp=int(input())
        cols.append(temp)
        

    print(2,flush=True)
    # for i in range(60):
    #     for j in range(60):
    #         print(b[i][j],end=' ',flush=True)
    #     print()

    print(FindMatrix(rows,cols,0,0,60,60,matrix),flush=True)
    verdict=int(input())
    if verdict==-1:
        exit()