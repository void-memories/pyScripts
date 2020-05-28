def convert(list): 
      
    # Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res)

t=int(input())
while t:
    t-=1
    a,b=input().split()
    init=int(a)+int(b)
    
    l1 = [int(x) for x in a] 
    l2= [int(x) for x in b]
    

    
    
    # if len(l1)<len(l2):
    #     for  i in range(len(l2)-len(l1)):
    #         l1.insert(0,0)
    # else:
    #     for  i in range(len(l1)-len(l2)):
    #         l2.insert(0,0)
    # print(l1,l2)
    
    
    t1=l1.copy()
    t2=l2.copy()
    
    z1=l1.copy()
    z2=l2.copy()
    
    
    
    for i in range(len(l1)):
        if len(l1)!=len(l2):
            start=i
        else:
            start=i+1
        for j in range(start,len(l2)):
            if l1[i]<l2[i]:
                t1[i],t2[j]=t2[j],t1[i]
                break
    
            
    for i in range(len(l2)):
        if len(l1)!=len(l2):
            start=i
        else:
            start=i+1
        for j in range(start,len(l1)):
            if l2[i]<l1[j]:
                z1[j],z2[i]=z2[i],z1[j]
                break
    #print(z1,z2,t1,t2)
            
    sum1=0
    sum2=0
    
    t1=convert(t1)
    t2=convert(t2)
    z1=convert(z1)
    z2=convert(z2)
    #print(t1,t2,z1,z2)
    
    print(max(t1+t2,z1+z2,init))
    
        
    
        
    
            
    
