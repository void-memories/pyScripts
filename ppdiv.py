import math
m=1000000007
def powerNumbers(n):

    v =set()
    v.add(1)

    for i in range(2,1000001):
        pc=3
        temp=pow(i,2)
        v.add(temp)
        while (pow(i,pc) <= (n)):
            temp=pow(i,pc)
            
            if temp>1e18:
                yy=int(math.sqrt(temp))
                if yy*yy!=temp:
                    v.add(temp)
            else:
                v.add(temp)
            pc+=1
    
    return v

ar=powerNumbers(1000000000000000000)
ar=sorted(ar)
s=0
t=int(input())
while t:
    n=int(input())
    t-=1
    sumi=0
    dc=set()
    # print(len(ar))
    if n<=1000000000000:
        for i in ar:
            if n>=i:
                sumi=(sumi+(i*math.floor(n/i))%m)
            else:
                break
        print(int(sumi)%m)
    else:
        for i in ar:
            if n>=i:
                sumi=(sumi+(i*math.floor(n/i))%m)
            else:
                break
            
        breaks=[]
        max_value=math.floor(n/(1000001*1000001))
        # print(max_value)
        max_value_p=[]

        
        while max_value>=1:
            b=(math.sqrt((n//max_value)))
            breaks.append(math.floor(b))
            max_value_p.append(max_value)
            max_value=(math.floor(n/(((math.floor(b)+1))*(math.floor(b)+1))))

        max_value_p.sort(reverse=True)
        breaks.sort()
        # print(max_value_p)
        # print(len(breaks),len(max_value_p))
        # for i in range(len(breaks)):
        #     print(breaks[i],max_value_p[i])

        
        curr=0
        final=0
        start=1000000
        for i in range(len(breaks)):
            start+=1
            # prev=start
            end=breaks[i]
            # print(start,end,max_value_p[curr])
            # end=breaks[i+1]
            due=start-1
            
            a=(((due)))
            b=(a+1)
            c=((2*a)+1)
            d=pow(6,m-2,m)
            
            a1=(((end)))
            b1=(a1+1)
            c1=((2*a1)+1)
            d1=pow(6,m-2,m)
            # print(a,b,c,d,a1,b1,c1,d1)
            first=((((((a1*b1))*c1))//6))
            second=((((((a*b))*c))//6))
            catalyst=(max_value_p[curr])
            
            f=(((first-second))*catalyst)
            
            final=(final+f)%m
            curr+=1
            start=end
        print((int(final+sumi))%m)
        # print(end,catalyst)
        
