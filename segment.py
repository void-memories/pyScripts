arr=[1,5,2,4,3]
tree=[0]*20

def build(node,low,high):
    if low==high:
        tree[node]=arr[low]
        return

    else:
        mid=(low+high)//2
        build(2*node,low,mid)
        build(2*node+1,mid+1,high)
        tree[node]=tree[2*node]+tree[2*node+1]

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
        tree[node]=tree[2*node]+tree[2*node+1]

def query(node,low,high,l,r):
    if r<low or high<l:
        return 0
    if l<=low and high<=r:
        return tree[node]
    mid=(low+high)//2
    p1=query(2*node,low,mid,l,r)
    p2=query(2*node+1,mid+1,high,l,r)
    return (p1+p2)

build(1,0,4)
print(tree)

