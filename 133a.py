s=input()
flag=0
for i in s:
    if i=='H' or i=='Q' or i=='9':
        print('YES')
        flag=1
        break
if not flag:
    print('NO')
