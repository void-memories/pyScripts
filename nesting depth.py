xxx=int(input())
for t in range(xxx):
    s=input()
    o=0
    c=0

    for i in range(len(s)-1):
        oi=0
        ci=0
        if s[i]!=0:
            if o<int(s[i]):
                oi=int(s[i])-o
                o+=oi
                
            
                for j in range(oi):
                    print('(',end='')
                print(s[i],end='')
            else:
                print(s[i],end='')
            ci=max(int(s[i])-int(s[i+1]),0)
            o-=ci
            for j in range(ci):
                print(')',end='')
            # print(s[i],end='')
        else:
            print(s[i],end='')
        
    o=0
    c=0
    i=len(s)-1
    if s[i]!=0:
        if o<int(s[i]):
            oi=int(s[i])-o
            o+=oi
            
        
            for j in range(oi):
                print('(',end='')
            print(s[i],end='')
        else:
            print(s[i],end='')
        # ci=max(int(s[i])-int(s[i+1]),0)
        # o-=ci
        for j in range(o):
            print(')',end='')
        # print(s[i],end='')
    else:
        print(s[i],end='')

            
