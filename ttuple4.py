import math

def ifDeno(a1,b1,c1,a2,b2,c2):
    
    if a2==b2==c2!=0:
        return True

    if a2==b2:
        if c1==c2:
            return True
        if c2==0:
            return True
        if c1+a2==c2:
            return True

    if b2==c2:
        if a1==a2:
            return True
        if a2==0:
            return True
        if a1+b2==a2:
            return True

    if c2==a2:
        if b1==b2:
            return True
        if b2==0:
            return True
        if b1+a2==b2:
            return True

    return False


def ifCombo(x,y,z,x2,y2,z2):
    if x+y==z or y+z==x or z+x==y:
        return True
    if x2==math.ceil(x2) and y2==math.ceil(y2) and z2==math.ceil(z2):
        if x2*y2==z2 or y2*z2==x2 or z2*x2==y2:
            return True

    return False


def ifTwoBrute2(a1,b1,c1,a2,b2,c2):
    up1=a2-a1
    up2=b2-b1
    up3=c2-c1

    down1=-a2-a1
    down2=-b2-b1
    down3=-c2-c1

    for i in range(min(up1,down1),max(up1,down1)+1):
        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and c2%(c1+i)==0 and a2//(a1+i)==b2//(b1+i)==c2//(c1+i):
                return True
        except:
            n=0

        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and a2//(a1+i)==b2//(b1+i):
                if c1==c2 or c1+i==c2 or c1*(a2//(a1+i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2%(b1+i)==0 and c2%(c1+i)==0 and b2//(b1+i)==c2//(c1+i):
                if a1==a2 or a1+i==a2 or a1*(b2//(b1+i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2%(c1+i)==0 and a2%(a1+i)==0 and c2//(c1+i)==a2//(a1+i):
                if b1==b2 or b1+i==b2 or b1*(a2//(a1+i))==b2:
                    return True
        except:
            n=0

    for i in range(min(up2,down2),max(up2,down2)+1):
        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and c2%(c1+i)==0 and a2//(a1+i)==b2//(b1+i)==c2//(c1+i):
                return True
        except:
            n=0

        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and a2//(a1+i)==b2//(b1+i):
                if c1==c2 or c1+i==c2 or c1*(a2//(a1+i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2%(b1+i)==0 and c2%(c1+i)==0 and b2//(b1+i)==c2//(c1+i):
                if a1==a2 or a1+i==a2 or a1*(b2//(b1+i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2%(c1+i)==0 and a2%(a1+i)==0 and c2//(c1+i)==a2//(a1+i):
                if b1==b2 or b1+i==b2 or b1*(a2//(a1+i))==b2:
                    return True
        except:
            n=0

    for i in range(min(up3,down3),max(up3,down3)+1):
        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and c2%(c1+i)==0 and a2//(a1+i)==b2//(b1+i)==c2//(c1+i):
                return True
        except:
            n=0

        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and a2//(a1+i)==b2//(b1+i):
                if c1==c2 or c1+i==c2 or c1*(a2//(a1+i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2%(b1+i)==0 and c2%(c1+i)==0 and b2//(b1+i)==c2//(c1+i):
                if a1==a2 or a1+i==a2 or a1*(b2//(b1+i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2%(c1+i)==0 and a2%(a1+i)==0 and c2//(c1+i)==a2//(a1+i):
                if b1==b2 or b1+i==b2 or b1*(a2//(a1+i))==b2:
                    return True
        except:
            n=0

    


    for i in range(min(up1,down1),max(up1,down1)+1):
        try:
            if a2-(a1*i)==b2-(b1*i)==c2-(c1*i):
                return True
        except:
            n=0
            
        try:
            if a2-(a1*i)==b2-(b1*i):
                if c1==c2 or c1*i==c2 or c1+(a2-(a1*i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2-(b1*i)==c2-(c1*i):
                if a1==a2 or a1*i==a2 or a1+(b2-(b1*i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2-(c1*i)==a2-(a1*i):
                if b1==b2 or b1*i==b2 or b1+(c2-(c1*i))==b2:
                    return True
        except:
            n=0

    for i in range(min(up2,down2),max(up2,down2)+1):
        try:
            if a2-(a1*i)==b2-(b1*i)==c2-(c1*i):
                return True
        except:
            n=0
            
        try:
            if a2-(a1*i)==b2-(b1*i):
                if c1==c2 or c1*i==c2 or c1+(a2-(a1*i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2-(b1*i)==c2-(c1*i):
                if a1==a2 or a1*i==a2 or a1+(b2-(b1*i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2-(c1*i)==a2-(a1*i):
                if b1==b2 or b1*i==b2 or b1+(c2-(c1*i))==b2:
                    return True
        except:
            n=0

    for i in range(min(up3,down3),max(up3,down3)+1):
        try:
            if a2-(a1*i)==b2-(b1*i)==c2-(c1*i):
                return True
        except:
            n=0
            
        try:
            if a2-(a1*i)==b2-(b1*i):
                if c1==c2 or c1*i==c2 or c1+(a2-(a1*i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2-(b1*i)==c2-(c1*i):
                if a1==a2 or a1*i==a2 or a1+(b2-(b1*i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2-(c1*i)==a2-(a1*i):
                if b1==b2 or b1*i==b2 or b1+(c2-(c1*i))==b2:
                    return True
        except:
            n=0

    return False


    
def ifTwoBrute(a1,b1,c1,a2,b2,c2):
    up1=a2-a1
    up2=b2-b1
    up3=c2-c1

    down1=-a2-a1
    down2=-b2-b1
    down3=-c2-c1

    upCurrent=0
    downCurrent=0
    status=[False,False,False]
    status1=[False,False,False]

    if a1==a2:
        upCurrent+=1
        downCurrent+=1
        status[0]=True
        status1[0]=True
    if b1==b2:
        upCurrent+=1
        downCurrent+=1
        status[1]=True
        status1[1]=True
    if c1==c2:
        upCurrent+=1
        downCurrent+=1
        status[2]=True
        status1[2]=True

    i=0
    while(upCurrent<2):
        if i>up1 and status[0]==False:
            upCurrent+=1
            status[0]=True
        if i>up2 and status[1]==False:
            upCurrent+=1
            status[1]=True
        if i>up3 and status[2]==False:
            upCurrent+=1
            status[2]=True

        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and c2%(c1+i)==0 and a2//(a1+i)==b2//(b1+i)==c2//(c1+i):
                return True
        except:
            n=0

        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and a2//(a1+i)==b2//(b1+i):
                if c1==c2 or c1+i==c2 or c1*(a2//(a1+i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2%(b1+i)==0 and c2%(c1+i)==0 and b2//(b1+i)==c2//(c1+i):
                if a1==a2 or a1+i==a2 or a1*(b2//(b1+i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2%(c1+i)==0 and a2%(a1+i)==0 and c2//(c1+i)==a2//(a1+i):
                if b1==b2 or b1+i==b2 or b1*(a2//(a1+i))==b2:
                    return True
        except:
            n=0

        i+=1

    i=0
    while(downCurrent<2):
        if i<down1 and status1[0]==False:
            downCurrent+=1
            status1[0]=True
        if i<down2 and status1[1]==False:
            downCurrent+=1
            status1[1]=True
        if i<down3 and status1[2]==False:
            downCurrent+=1
            status1[2]=True

        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and c2%(c1+i)==0 and a2//(a1+i)==b2//(b1+i)==c2//(c1+i):
                return True
        except:
            n=0
            
        try:
            if a2%(a1+i)==0 and b2%(b1+i)==0 and a2//(a1+i)==b2//(b1+i):
                if c1==c2 or c1+i==c2 or c1*(a2//(a1+i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2%(b1+i)==0 and c2%(c1+i)==0 and b2//(b1+i)==c2//(c1+i):
                if a1==a2 or a1+i==a2 or a1*(b2//(b1+i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2%(c1+i)==0 and a2%(a1+i)==0 and c2//(c1+i)==a2//(a1+i):
                if b1==b2 or b1+i==b2 or b1*(a2//(a1+i))==b2:
                    return True
        except:
            n=0
        
        i-=1

    up1=a2-a1
    up2=b2-b1
    up3=c2-c1

    down1=-a2-a1
    down2=-b2-b1
    down3=-c2-c1

    upCurrent=0
    downCurrent=0
    status=[False,False,False]
    status1=[False,False,False]

    if a1==a2:
        upCurrent+=1
        downCurrent+=1
        status[0]=True
        status1[0]=True
    if b1==b2:
        upCurrent+=1
        downCurrent+=1
        status[1]=True
        status1[1]=True
    if c1==c2:
        upCurrent+=1
        downCurrent+=1
        status[2]=True
        status1[2]=True

    i=0
    while(upCurrent<2):
        if i>up1 and status[0]==False:
            upCurrent+=1
            status[0]=True
        if i>up2 and status[1]==False:
            upCurrent+=1
            status[1]=True
        if i>up3 and status[2]==False:
            upCurrent+=1
            status[2]=True

        try:
            if a2-(a1*i)==b2-(b1*i)==c2-(c1*i):
                return True
        except:
            n=0
            
        try:
            if a2-(a1*i)==b2-(b1*i):
                if c1==c2 or c1*i==c2 or c1+(a2-(a1*i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2-(b1*i)==c2-(c1*i):
                if a1==a2 or a1*i==a2 or a1+(b2-(b1*i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2-(c1*i)==a2-(a1*i):
                if b1==b2 or b1*i==b2 or b1+(c2-(c1*i))==b2:
                    return True
        except:
            n=0

        i+=1

    
    i=0
    while(downCurrent<2):
        if i<down1 and status1[0]==False:
            downCurrent+=1
            status1[0]=True
        if i<down2 and status1[1]==False:
            downCurrent+=1
            status1[1]=True
        if i<down3 and status1[2]==False:
            downCurrent+=1
            status1[2]=True

        try:
            if a2-(a1*i)==b2-(b1*i)==c2-(c1*i):
                return True
        except:
            n=0
            
        try:
            if a2-(a1*i)==b2-(b1*i):
                if c1==c2 or c1*i==c2 or c1+(a2-(a1*i))==c2:
                    return True
        except:
            n=0
        
        try:
            if b2-(b1*i)==c2-(c1*i):
                if a1==a2 or a1*i==a2 or a1+(b2-(b1*i))==a2:
                    return True
        except:
            n=0
        
        try:
            if c2-(c1*i)==a2-(a1*i):
                if b1==b2 or b1*i==b2 or b1+(c2-(c1*i))==b2:
                    return True
        except:
            n=0
        
        i-=1

    return False
        


        

        


def ifTwo(a1,b1,c1,a2,b2,c2):

    ints=[]
    try:
        if a2!=b2 and a1!=b1:
            if (a2-b2)%(a1-b1)==0:
                x=(a2-b2)//(a1-b1)
                if a2-a1*x==b2-b1*x:
                    ints.append(x)
    except:
        n=0
    
    try:
        if b2!=c2 and b1!=c1:
            if (b2-c2)%(b1-c1)==0:
                x=(b2-c2)//(b1-c1)
                if b2-b1*x==c2-c1*x:
                    ints.append(x)
    except:
        n=0
    
    try:
        if c2!=a2 and c1!=a1:
            if (c2-a2)%(c1-a1)==0:
                x=(c2-a2)//(c1-a1)
                if c2-c1*x==a2-a1*x:
                    ints.append(x)
    except:
        n=0


    if len(ints)==3 and len(set(ints))==1:
        return True
    if len(ints)==3 and len(set(ints))==2:
        return True

    if len(ints)==3 and len(set(ints))==3:

        try:
            x=(a2-b2)//(a1-b1)
            y=a2-a1*x
            xx=(a1*b2-a2*b1)//(a2-b2)
            yy=a2//(a1+xx)
            if c1==c2 or c1+y==c2 or c1*x==c2 or c1+xx==c2 or c1*yy==c2:
                return True
        except:
            n=0


        try:
            x=(b2-c2)//(b1-c1)
            y=b2-b1*x
            xx=(b1*c2-b2*c1)//(b2-c2)
            yy=b2//(b1+xx)
            if a1==a2 or a1+y==a2 or a1*x==a2 or a1+xx==a2 or a1*yy==a2:
                return True
        except:
            n=0

        try:
            x=(c2-a2)//(c1-a1)
            y=c2-c1*x
            xx=(c1*a2-c2*a1)//(c2-a2)
            yy=c2//(c1+xx)
            if b1==b2 or b1+y==b2 or b1*x==b2 or b1+xx==b2 or b1*yy==b2:
                return True
        except:
            n=0

    if len(ints)==2 and len(set(ints))==1:
        return True
    
    if (len(ints)==2 and len(set(ints))==2) or len(ints)==1:
        try:
            if a2!=b2 and a1!=b1:
                if (a2-b2)%(a1-b1)==0:
                    x=(a2-b2)//(a1-b1)
                    if a2-a1*x==b2-b1*x:
                        y=a2-a1*x
                        xx=(a1*b2-a2*b1)//(a2-b2)
                        yy=a2//(a1+xx)
                        if c1==c2 or c1+y==c2 or c1*x==c2 or c1+xx==c2 or c1*yy==c2:
                            return True
        except:
            n=0


        try:
            if b2!=c2 and b1!=c1:
                if (b2-c2)%(b1-c1)==0:
                    x=(b2-c2)//(b1-c1)
                    if b2-b1*x==c2-c1*x:
                        y=b2-b1*x
                        xx=(b1*c2-b2*c1)//(b2-c2)
                        yy=b2//(b1+xx)
                        if a1==a2 or a1+y==a2 or a1*x==a2 or a1+xx==a2 or a1*yy==a2:
                            return True
        except:
            n=0

        try:        
            if c2!=a2 and c1!=a1:
                if (c2-a2)%(c1-a1)==0:
                    x=(c2-a2)//(c1-a1)
                    if c2-c1*x==a2-a1*x:
                        y=c2-c1*x
                        xx=(c1*a2-c2*a1)//(c2-a2)
                        yy=c2//(c1+xx)
                        if b1==b2 or b1+y==b2 or b1*x==b2 or b1+xx==b2 or b1*yy==b2:
                            return True
        except:
            n=0

    return False

    


def ifGrid(a1,b1,c1,a2,b2,c2):
    l=[[None,None,None],[None,None,None]]
    l[0][0]=a2-a1
    l[0][1]=b2-b1
    l[0][2]=c2-c1

    try:
        if a2%a1==0:
            l[1][0]=a2//a1
    except:
        n=0
    
    try:
        if b2%b1==0:
            l[1][1]=b2//b1
    except:
        n=0
    
    try:
        if c2%c1==0:
            l[1][2]=c2//c1
    except:
        n=0

    if l[0][1]!=None and l[1][2]!=None:
        if (a1+l[0][1])*l[1][2]==a2 or l[0][1]+(a1*l[1][2])==a2: 
            return True
    
    if l[0][2]!=None and l[1][1]!=None:
        if (a1+l[0][2])*l[1][1]==a2 or l[0][2]+(a1*l[1][1])==a2:
            return True
    
    if l[0][0]!=None and l[1][2]!=None:
        if (b1+l[0][0])*l[1][2]==b2 or l[0][0]+(b1*l[1][2])==b2: 
            return True
    
    if l[0][2]!=None and l[1][0]!=None:
        if (b1+l[0][2])*l[1][0]==b2 or l[0][2]+(b1*l[1][0])==b2:
            return True

    if l[0][0]!=None and l[1][1]!=None:
        if (c1+l[0][0])*l[1][1]==c2 or l[0][0]+(c1*l[1][1])==c2: 
            return True
    
    if l[0][1]!=None and l[1][0]!=None:
        if (c1+l[0][1])*l[1][0]==c2 or l[0][1]+(c1*l[1][0])==c2:
            return True

    return False
    

        
     


t = int(input())
while t:
    t -= 1
    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())

    ones=0
    zeros=0

    x=a2-a1
    y=b2-b1
    z=c2-c1


    withoutZeros=[]
    withoutOnes=[]
    onlyInts=[]

    if x==0:
        zeros+=1
    else:
        withoutZeros.append(x)
    if y==0:
        zeros+=1
    else:
        withoutZeros.append(y)
    if z==0:
        zeros+=1
    else:
        withoutZeros.append(z)




    try:
        if a2%a1==0:
            x2=a2//a1
        else:
            x2=8.12248952
    except:
        x2=8.12248952

    try:
        if b2%b1==0:
            y2=b2//b1
        else:
            y2=43.82248952
    except:
        y2=43.82248952

    try:
        if c2%c1==0:
            z2=c2//c1
        else:
            z2=3.81118952
    except:
        z2=3.81118952

    
    if x2==1:
        ones+=1
    if y2==1:
        ones+=1
    if z2==1:
        ones+=1

    if x2!=1 and math.ceil(x2)==x2 and x2!=0:
        withoutOnes.append(x2)

    if y2!=1 and math.ceil(y2)==y2 and y2!=0:
        withoutOnes.append(y2)
        
    if z2!=1 and math.ceil(z2)==z2 and z2!=0:
        withoutOnes.append(z2)

    if math.ceil(x2)==x2:
        onlyInts.append(x2)
    if math.ceil(y2)==y2:
        onlyInts.append(y2)
    if math.ceil(z2)==z2:
        onlyInts.append(z2)


    # if math.ceil(x2)==x2 and x2!=0:
    #     onlyInts.append(x2)
    # if math.ceil(y2)==y2 and y2!=0:
    #     onlyInts.append(y2)
    # if math.ceil(z2)==z2 and z2!=0:
    #     onlyInts.append(z2)


    # print(withoutOnes,withoutZeros)
    if x==y==z==0:
        print(0)

    elif len(set(withoutZeros))==1:
        print(1)
    elif len(withoutOnes)+ones==3 and len(set(withoutOnes))==1:
        print(1)
        
    elif a2==b2==c2==0:
        print(1)
    elif a2==b2==0 and c1==c2:
        print(1)
    elif b2==c2==0 and a1==a2:
        print(1)
    elif c2==a2==0 and b1==b2:
        print(1)
    

    elif ifTwoBrute2(a1,b1,c1,a2,b2,c2) or ifCombo(x,y,z,x2,y2,z2) or ifDeno(a1,b1,c1,a2,b2,c2) or ifGrid(a1,b1,c1,a2,b2,c2):
        print(2)
    elif (x==y or y==z or z==x) and zeros==0:
        print(2)
    elif (x!=y and y!=z and z!=x and zeros==1):
        print(2)
    elif len(onlyInts)==3 and len(set(onlyInts))==2 and ones==0:
        print(2)
    elif len(onlyInts)==3 and len(set(onlyInts))==3 and ones==1:
        print(2)
    elif len(onlyInts)==2 and len(set(onlyInts))==1 and ones==0:
        print(2)
    elif len(onlyInts)==2 and len(set(onlyInts))==2 and ones==1:
        print(2)
    elif len(onlyInts)==1 and ones==1:
        print(2)

    # elif ones==0 and len(withoutOnes)==len(set(withoutOnes)) and zeros==0 and len(withoutZeros)==len(set(withoutZeros)):
    #     print(3)

    # else:
    #     print(2)
    else:
        print(3)
    