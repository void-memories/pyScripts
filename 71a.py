n=int(input())
while n:
    n-=1
    word=input()
    if len(word)>10:
        print(word[0]+str(len(word)-2)+word[len(word)-1],sep='')
    else:
        print(word)
