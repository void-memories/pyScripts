import math


def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        else: 
            r = mid - 1
      
    return -1
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 





n=int(input())
beg1=1
end1=n

beg2=1
end2=n
prev=0
flag=0
ar=[]

for i in range(1000000):
    ar.append(i+1)

l=0
r=len(ar)-1

inp1=input()








# for i in range(300):
#     print(math.floor((beg1+end1)/2),flush=True)
#     # print(beg1,end1)
#     inp1=input()
    

#     if inp1==prev or inp1=='E':
#         if inp1=='G':
#             beg1=math.ceil((beg1+end1)/2)
            
#         elif inp1=='L':
#             end1=math.floor((beg1+end1)/2)
#         else:
#             flag=1
#             exit()
            
#     prev=inp1

# if flag==0:
#     print(0//0)

