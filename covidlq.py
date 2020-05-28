t=int(input())
while t:
    flag=0
    start=-1
    t-=1
    n=int(input())
    ar=input()

    for i in range(n):
        if ar[i]=='1':
            if start!=-1:
                if e-start<6:
                    flag=1
                    break
                else:
                    start=i
    print('YES' if not flag else 'NO')
