import math

def fnAdd(x,y,z):
    zero=0
    if x==0:
        zero+=1
    if y==0:
        zero+=1
    if z==0:
        zero+=1
    
    l=[x,y,z]

    if len(set(l))==1 and zero==3:
        return 0
    
    elif len(set(l))==1 and zero==0:
        return 1


    elif len(set(l))==2 and zero==1:
        return 1
    
    elif len(set(l))==2 and zero==2:
        return 1

    elif len(set(l))==2 and zero==0:
        return 2
    
    elif len(set(l))==3 and zero==1:
        return 2
    
    elif len(set(l))==3 and zero==0:
        return 3

    return 3



def fnMul(x,y,z):
    ones=0
    if x==1:
        ones+=1
    if y==1:
        ones+=1
    if z==1:
        ones+=1
    
    l=[x,y,z]

    if len(set(l))==1 and ones==3:
        return 0
    
    elif len(set(l))==1 and ones==0:
        return 1


    elif len(set(l))==2 and ones==1:
        return 1
    
    elif len(set(l))==2 and ones==2:
        return 1

    elif len(set(l))==2 and ones==0:
        return 2
    
    elif len(set(l))==3 and ones==1:
        return 2
    
    elif len(set(l))==3 and ones==0:
        return 3

    return 3


def fnDeno(a,b,c,d,e,f):
    zero=0
    if d==0:
        zero+=1
    if e==0:
        zero+=1
    if f==0:
        zero+=1

    l=[d,e,f]

    if len(set(l))==1 and zero==3:
        return 1
    
    if len(set(l))==1 and zero==0:
        return 2
    
    if len(set(l))==2 and zero==2:
        if d!=0:
            if d==a:
                return 1
            else:
                return 2

        if e!=0:
            if e==b:
                return 1
            else:
                return 2

        if f!=0:
            if f==c:
                return 1
            else:
                return 2
    
    if len(set(l))==2 and zero==1:
        return 2

    if len(set(l))==2 and zero==0:
        if l.count(d)==1:
            if a==d or ((d-a)==e):
                return 2

        if l.count(e)==1:
            if b==e or ((e-b)==f):
                return 2

        if l.count(f)==1:
            if c==f or ((f-c)==d):
                return 2
                
    return 3


def fnComb(a,b,c,d,e,f):

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
    
    
    # print(ints)
    if len(ints)==3 and len(set(ints))==1:
        return 2

    if len(ints)==3 and len(set(ints))==2:
        return 2 

    if len(ints)==3 and len(set(ints))==3:

        try:
            x=((b*f)-(c*e))//(e-f)
            if (a==d or (d//(a)==e//(b+x)) or (a+x==d)) and b!=c and e%(b+x)==0 and f%(c+x)==0:
                return 2
        except:
            nothing=0


        try:
            x=((c*d)-(a*f))//(f-d)
            if (b==e or (e//(b)==d//(a+x)) or (b+x==e)) and c!=a and f%(c+x)==0 and d%(a+x)==0:
                return 2
        except:
            nothing=0

        
        try:
            x=((a*e)-(b*d))//(d-e)
            if (c==f or (f//(c)==e//(b+x)) or (c+x==f)) and a!=b and d%(a+x)==0 and e%(b+x)==0:
                return 2
        except:
            nothing=0

    if len(ints)==2 and len(set(ints))==1:
        return 2
    if len(ints)==2 and len(set(ints))==2:
        try:
            x=((b*f)-(c*e))/(e-f)
            if (a==d or (d//(a)==e//(b+x)) or (a+x==d)) and b!=c and math.ceil(x)==x and e%(b+x)==0 and f%(c+x)==0:
                return 2
        except:
            nothing=0


        try:
            x=((c*d)-(a*f))/(f-d)
            if (b==e or (e//(b)==d//(a+x)) or (b+x==e)) and c!=a and math.ceil(x)==x and f%(c+x)==0 and d%(a+x)==0:
                return 2
        except:
            nothing=0

        
        try:
            x=((a*e)-(b*d))/(d-e)
            if (c==f or (f//(c)==e//(b+x)) or (c+x==f)) and a!=b and math.ceil(x)==x and d%(a+x)==0 and e%(b+x)==0:
                return 2
        except:
            nothing=0


    if len(ints)==1:
        try:
            x=((b*f)-(c*e))/(e-f)
            if (a==d or (d//(a)==e//(b+x)) or (a+x==d)) and b!=c and math.ceil(x)==x and e%(b+x)==0 and f%(c+x)==0:
                return 2
        except:
            nothing=0


        try:
            x=((c*d)-(a*f))/(f-d)
            if (b==e or (e//(b)==d//(a+x)) or (b+x==e)) and c!=a and math.ceil(x)==x and f%(c+x)==0 and d%(a+x)==0:
                return 2
        except:
            nothing=0

        
        try:
            x=((a*e)-(b*d))/(d-e)
            if (c==f or (f//(c)==e//(b+x)) or (c+x==f)) and a!=b and math.ceil(x)==x and d%(a+x)==0 and e%(b+x)==0:
                return 2
        except:
            nothing=0

    

    return 3
    

    
def ifCombo(x,y,z,x2,y2,z2):
    if x+y==z or y+z==x or z+x==y:
        return 2
    if x2*y2==z2 or y2*z2==x2 or x2*z2==y2:
        return 2
    return 3


t = int(input())
while t:
    t -= 1
    a, b, c = map(int, input().split())
    d, e, f = map(int, input().split())

    ad=3
    mul=3
    deno=3
    comb=3

    ad=fnAdd(d-a,e-b,f-c)

    try:
        if d%a==0:
            x=d//a
        else:
            x=3.8464537382846
    except:
        x=3.8464537382846

    try:
        if e%b==0:
            y=e//b
        else:
            y=8.8464583382846
    except:
        y=8.8464583382846

    try:
        if f%c==0:
            z=f//c
        else:
            z=1.8036537382846
    except:
        z=1.8036537382846

    mul=fnMul(x,y,z)
    deno=fnDeno(a,b,c,d,e,f)
    comb=fnComb(a,b,c,d,e,f)
    combo=ifCombo(d-a,e-b,f-c,x,y,z)

    print(min(ad,mul,deno,comb,combo))
