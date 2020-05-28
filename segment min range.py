n,q=input().split()
n,q=int(n),int(q)
tree=[float('inf')]*(2000005)
arr=list(map(int,input().split()))

def build(node,low,high):
    if low==high:
        tree[node]=arr[low]

    else:
        mid=(low+high)//2
        build(2*node,low,mid)
        build(2*node+1,mid+1,high)
        tree[node]=min(tree[2*node],tree[2*node+1])

def update(node,low,high,idx,val):
    if low==high:
        arr[idx]=val
        tree[node]=val

    else:
        mid=(low+high)//2
        if(low<=idx and idx<=mid):
            update(2*node,low,mid,idx,val)
        else:
            update(2*node+1,mid+1,high,idx,val)
        tree[node]=min(tree[2*node],tree[2*node+1])

def query(node,low,high,l,r):
    if r<low or high<l:
        return float('inf')
    if l<=low and high<=r:
        return tree[node]
    mid=(low+high)//2
    p1=query(2*node,low,mid,l,r)
    p2=query(2*node+1,mid+1,high,l,r)
    #print(p1,p2)
    return min(p1,p2)

build(1,0,n-1)
#print(tree)
for i in range(q):
    a,b,c=input().split()
    b,c=int(b),int(c)
    
    if a=='q':
        print(query(1,0,n-1,b-1,c-1))
    else:
        update(1,0,n-1,b-1,c)
        #print(tree)
        
    