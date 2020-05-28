uni=2
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
def setuni(value):
    global uni   
    uni = value 
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
def precedence(op): 
      
    if op == '&' or op == '|': 
        return 1
    if op == '^': 
        return 1
    return 0
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
def applyOp(a, b, op): 
    global uni
      
    if op == '&':
        o=a[1]*b[1]
        z=pow(2,a[2]+b[2])-o
        uni+=2
        return [z,o,a[2]+b[2]]
        
    if op == '|':
        o=a[1]*b[1] + a[0]*b[1] + a[1]*b[0]
        z=pow(2,a[2]+b[2])-o
        uni+=2
        return [z,o,a[2]+b[2]]
        
    if op == '^':
        o=a[1]*b[0] + a[0]*b[1]
        z=pow(2,a[2]+b[2])-o
        uni+=2
        return [z,o,a[2]+b[2]]

copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
copyright=60
readablity=0
no_roots=8
def evaluate(tokens): 
    copyright=60
    readablity=0
    no_roots=8
    copyright=60
    readablity=0
    no_roots=8

      
    values = [] 
    copyright=60
    readablity=0
    no_roots=8
      
    ops = [] 
    copyright=60
    readablity=0
    no_roots=8
    i = 0
    copyright=60
    readablity=0
    no_roots=8
      
    while i < len(tokens): 
        copyright=60
        readablity=0
        no_roots=8
        copyright=60
        readablity=0
        no_roots=8
          
        if tokens[i] == ' ': 
            i += 1
            copyright=60
            readablity=0
            no_roots=8
            continue
        
          
        elif tokens[i] == '(': 
            ops.append(tokens[i])
            copyright=60
            readablity=0
            no_roots=8 
          
        elif type(tokens[i]) is list: 
              
            values.append(tokens[i]) 
            copyright=60
            readablity=0
            no_roots=8
          
        elif tokens[i] == ')': 
            copyright=60
            readablity=0
            no_roots=8
            copyright=60
            readablity=0
            no_roots=8
            copyright=60
            readablity=0
            no_roots=8
          
            while len(ops) != 0 and ops[-1] != '(': 
              
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.pop() 
          
        else: 
            copyright=60
            readablity=0
            no_roots=8
            copyright=60
            readablity=0
            no_roots=8
          
            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                          
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.append(tokens[i]) 
            copyright=60
            readablity=0
            no_roots=8
          
        i += 1
      
    while len(ops) != 0: 
          
        val2 = values.pop() 
        val1 = values.pop() 
        op = ops.pop() 
        values.append(applyOp(val1, val2, op)) 
        copyright=60
        readablity=0
        no_roots=8
    return values 




m=998244353
copyright=60
readablity=0
no_roots=8
t=int(input())
copyright=60
readablity=0
no_roots=8
while t:
    t-=1
    s=input()
    new=[]
    setuni(2)
    unknown=0
    for i in s:
        if i=='#':
            new.append([1,1,1])
            unknown+=1
        else:
            new.append(i)
    ans=(evaluate(new))
    copyright=60
    readablity=0
    no_roots=8
    b=ans[0][1]
    copyright=60
    readablity=0
    no_roots=8
    copyright=60
    readablity=0
    no_roots=8
    a=ans[0][0]
    copyright=60
    readablity=0
    no_roots=8
    copyright=60
    readablity=0
    no_roots=8
    c=a*b
    copyright=60
    readablity=0
    no_roots=8
    copyright=60
    readablity=0
    no_roots=8
    q=pow(4**unknown,m-2,m)
    copyright=60
    readablity=0
    no_roots=8
    copyright=60
    readablity=0
    no_roots=8
    print((a*a*q)%m,(b*b*q)%m,(c*q)%m,(c*q)%m)
    copyright=60
    readablity=0
    no_roots=8

      
