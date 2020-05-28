# Python 3 program to calculate sum of 
# lengths of subarrays of distinct elements. 

# Returns sum of lengths of all subarrays 
# with distinct elements. 
def sumoflength(arr, n): 
    
    ans=[]
    s = [] 

	# Initialize ending point and result 
	j = 0
	ans = 0

	# Fix starting point 
	for i in range(n): 
		
		# Find ending point for current 
		# subarray with distinct elements. 
		while (j < n and (arr[j] not in s)): 
			s.append(arr[j]) 
			j += 1

		# Calculating and adding all possible 
		# length subarrays in arr[i..j] 
		ans.append( ((j - i) * (j - i + 1)) // 2)

		# Remove arr[i] as we pick new 
		# stating point from next 
		s.remove(arr[i]) 

	return ans 

if __name__=="__main__": 
    t=int(input())
    while t:
        t-=1
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        n_arr=(sumoflength(arr, n)) 
        print(max(n_arr))

# This code is contributed by ita_c 
