y=int(input())
i=1
while 1:
    flag=1
    n=i
    while(n//10!=0):
        a=n%10
        n//=10
        if (a-n%10)==0 or (a-n%10)==-1 or (a-n%10)==1:
            donothing=1
        else:
            flag=0

    if flag:
        cnt+=1
    if cnt==y:
        break
    i+=1
print(i)