for i in range(5):
    ar=list(map(int,input().split()))
    for j in range(5):
        if ar[j]==1:
            row=j
            col=i
            break
print((abs(2-row)+abs(2-col)))
