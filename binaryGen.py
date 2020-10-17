def colSum(mat,n,c):
    sum=0
    for i in range(n):
        sum+=mat[i][c]
    return sum


n=5
row=[3,4,1,1,3]
col=[3,2,4,1,2]

t1=row
t2=col

matrix=[]
for i in range(n):
    tempo=[]
    for j in range(n):
        tempo.append(0)
    matrix.append(tempo)



for i in range(n):
    toWork=row[i]
    for j in range(toWork):
        matrix[i][j]=1

for i in range(n):
    if colSum(matrix,n,i)>col[i]:
        for j in range(n):
            if colsum(matrix,n,j)<col[j]