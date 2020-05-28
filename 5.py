n=int(input())
s=input()
a,b=input().split()
b=int(b)

org=[]
enc=[]
i=a
z=1
while((ord(i) + z)<=90):
    org.append(i)
    enc.append(chr(ord(i) + z))
    i=chr(ord(i)+1)
    z+=1
#print(org,enc)

for letter in s:
    for letter2 in range(len(enc)):
        if letter==enc[letter2]:
            print(org[letter2],sep='',end='')
print()
