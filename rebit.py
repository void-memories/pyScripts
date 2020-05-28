m=998244353
brr=[]
def printTheArray(arr, n): 

    brr.append(arr[0:n])
def generateAllBinaryStrings(n, arr, i): 

	if i == n: 
		printTheArray(arr, n) 
		return
	
	arr[i] = 0
	generateAllBinaryStrings(n, arr, i + 1) 

	arr[i] = 1
	generateAllBinaryStrings(n, arr, i + 1) 

# if __name__ == "__main__": 

# 	n = 4
# 	arr = [None] * n 

# 	generateAllBinaryStrings(n, arr, 0) 


t=int(input())
while t:
    t-=1
    s=input()
    unknown=0

    for i in s:
        if i=='#':
            unknown+=1
    
    arr=[None]*unknown
    brr=[]
    generateAllBinaryStrings(unknown,arr,0)
    ans=[]
    d={}
    d[0]=0
    d[1]=0
    d['a']=0
    d['A']=0
    
    
    
    for i in brr:
        inc=0
        exp=''
        for j in s:
            if j=='#':
                exp=exp+str(i[inc])
                inc+=1
            else:
                exp=exp+j
        ans.append(eval(exp))
        d[eval(exp)]+=1

    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            if ans[i]==ans[j]:
                d[ans[i]]+=1
            elif ans[i]==0 and ans[j]==1:
                d['a']+=1
            else:
                d['A']+=1
    ans=ans[::-1]
    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            if ans[i]==ans[j]:
                d[ans[i]]+=1
            elif ans[i]==0 and ans[j]==1:
                d['a']+=1
            else:
                d['A']+=1
    print(d)
    #print(ans)
    inv=pow(4**unknown,m-2,m)
    print((d[0]*inv)%m,end=' ')
    print((d[1]*inv)%m,end=' ')
    print((d['a']*inv)%m,end=' ')
    print((d['A']*inv)%m,end=' ')


    


