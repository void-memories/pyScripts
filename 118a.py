def is_v(c):
    v=['A','O','Y','E','U','I','a','o','y','e','u','i']
    return c in v

s=input()
new=[]

for i in s:
    if not is_v(i):
        new.append('.')
        new.append(i.lower())
for i in new:
    print(i,sep='',end='')
print()
