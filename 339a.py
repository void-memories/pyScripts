s=input()
a=[]
for i in s:
    if i!='+':
        a.append(i)
a.sort()
for i in a:
    print(a,end='+')

