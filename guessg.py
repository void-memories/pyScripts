import math

n=int(input())
beg1=1
end1=n

beg2=1
end2=n

detect=[1,n]
real=False
which=0

for i in range(300):
    session=0
    if real:
        print(math.floor((beg1+end1)/2),flush=True)
    else:
        print(detect[which])
        

    inp1=input()


    if real or inp1=='E':
        if inp1=='G':
            beg1=math.ceil((beg1+end1)/2)
        elif inp1=='L':
            end1=math.floor((beg1+end1)/2)
        else:
            exit()
        
        real=False
        session=1

    if session==0:
        if which:
            if inp1=='G':
                real=True
            else:
                if which:
                    which=0
                else:
                    which=1
        else:
            if inp1=='L':
                real=True
            else:
                if which:
                    which=0
                else:
                    which=1


    

    


    
    

    



            
