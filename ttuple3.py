import math


def ifDeno(a,b,c,d,e,f):
    if d==e==0 or e==f==0 or f==d==0:
        return True

    if d==e:
        if c==f or c+e==f or f==0:
            return True
    if e==f:
        if a==d or a+f==d or d==0:
            return True

    if f==d:
        if b==e or b+d==e or e==0:
            return True

    return False

def ifTwo(a,b,c,d,e,f):
    ints=[]
    try:
        if ((a*e)-(b*d))%(d-e)==0 and a!=b:
            xx=((a*e)-(b*d))//(d-e)
            if d%(a+xx)==0 and e%(b+xx)==0:
                ints.append(xx)
    except:
        nothing=0
    

    try:
        if ((b*f)-(c*e))%(e-f)==0 and b!=c:
            xx=((b*f)-(c*e))//(e-f)
            if e%(b+xx)==0 and f%(c+xx)==0:
                ints.append(xx)

            
    except:
        nothing=0
    

    try:
        if ((c*d)-(a*f))%(f-d)==0 and c!=a:
            xx=((c*d)-(a*f))//(f-d)
            if f%(c+xx)==0 and d%(a+xx)==0:
                ints.append(xx)
    except:
        nothing=0
        
    

    if (len(ints)==3 and len(set(ints))==1) or (len(ints)==3 and len(set(ints))==2):
        return True
    if (len(ints)==2 and len(set(ints))==1):
        return True
    if (len(ints)==2 and len(set(ints))==2) or len(ints)==1:
        try:
            if ((a*e)-(b*d))%(d-e)==0 and a!=b:
                xx=((a*e)-(b*d))//(d-e)
                if d%(a+xx)==0 and e%(b+xx)==0:
                    if c==f or (f%c==0 and f//c==e//(b+xx)) or (c+xx==f):
                        return True
        except:
            nothing=0
        

        try:
            if ((b*f)-(c*e))%(e-f)==0 and b!=c:
                xx=((b*f)-(c*e))//(e-f)
                if e%(b+xx)==0 and f%(c+xx)==0:
                    if a==d or (d%a==0 and d//a==e//(b+xx)) or (a+xx==d):
                        return True

                
        except:
            nothing=0
        

        try:
            if ((c*d)-(a*f))%(f-d)==0 and c!=a:
                xx=((c*d)-(a*f))//(f-d)
                if f%(c+xx)==0 and d%(a+xx)==0:
                    if b==e or (e%b==0 and e//b==f//(c+xx)) or (b+xx==e):
                        return True
        except:
            nothing=0
    return False


def ifCombo(x,y,z,x2,y2,z2):
    if x+y==z or y+z==x or z+x==y:
        return True
    if x2*y2==z2 or y2*z2==x2 or x2*z2==y2:
        return True
    return False

t = int(input())
while t:
    t -= 1
    a, b, c = map(int, input().split())
    d, e, f = map(int, input().split())

    ones=0
    zeros=0

    oneList=[]
    zeroList=[]

    x=d-a
    y=e-b
    z=f-c

    if x!=0:
        zeroList.append(x)
    if y!=0:
        zeroList.append(y)
    if z!=0:
        zeroList.append(z)

    if x==0:
        zeros+=1
    if y==0:
        zeros+=1
    if z==0:
        zeros+=1





    try:
        x2=d/a
    except:
        x2=1.8457

    try:
        y2=e/b
    except:
        y2=6.386

    try:
        z2=f/c
    except:
        z2=4.473




    if x2!=1 and x2!=0:
        oneList.append(x2)

    if y2!=1 and y2!=0:
        oneList.append(y2)

    if z2!=1 and z2!=0:
        oneList.append(z2)


    oneList2=[]


    if x2!=1 and math.ceil(x2)==x2 and x2!=0:
        oneList2.append(x2)

    if y2!=1 and math.ceil(y2)==y2 and y2!=0:
        oneList2.append(y2)

    if z2!=1 and math.ceil(z2)==z2 and z2!=0:
        oneList2.append(z2)


    if x2==1:
        ones+=1
    if y2==1:
        ones+=1
    if z2==1:
        ones+=1

    
    # print(ifTwo(a,b,c,d,e,f),ifDeno(a,b,c,d,e,f),oneList,oneList2,zeroList)
    if a==d and b==e and c==f:
        print(0)
    
    elif len(set(zeroList))==0 or len(set(zeroList))==1:
        print(1)
    
    elif len(set(oneList))==0 or (len(set(oneList))==1 and math.ceil(oneList[0])==oneList[0]):
        print(1)

    elif d==e==f==0:
        print(1)

    elif ifCombo(x,y,z,x2,y2,z2):
        print(2)

    
    elif ones==0 and len(set(oneList2))==len(oneList2) and zeros==0 and len(set(zeroList))==len(zeroList) and not ifTwo(a,b,c,d,e,f) and not ifDeno(a,b,c,d,e,f) and not d==e==f:
        print(3)

    else:
        print(2)