import math
n=int(input())
theCarryOvers=[]
theCarryOvers.append([1,n])
while(len(theCarryOvers)):
    temp=theCarryOvers.pop(0)
    low=temp[0]
    high=temp[1]
    prev=-1
    cnt=0
    while(high>=low):
        mid=(low+high)//2
        if prev==mid and cnt==0:
            break
        print(mid,flush=True)
        inp1=input()
        if inp1=='E':
            exit()
        else:
            print(mid,flush=True)
            inp2=input()
            if inp1=='E':
                exit()
            else:
                if inp1==inp2:
                    cnt+=1
                    if inp1=='L':
                        high=mid-1
                    elif inp1=='G':
                        low=mid+1
                else:
                    
                    theCarryOvers.append([mid+1,high])
                    theCarryOvers.append([low,mid-1])
                            
                            
        prev=mid

                        


