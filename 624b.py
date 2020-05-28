def bubbleSort(arr,br):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] and j+1 in br :
                arr[j], arr[j+1] = arr[j+1], arr[j]
t=int(input())
while t:
    t-=1
    flag=0
    n,m=map(int,input().split())
    ar=list(map(int,input().split()))
    br=list(map(int,input().split()))
    bubbleSort(ar,br)
    for i in range(n):
        if ar[i]>ar[i+1]:
            flag=1
            break
    print('YES' if flag==0 else 'NO')
