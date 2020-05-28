def precedence(op): 
      
    if op == '&' or op == '|': 
        return 1
    if op == '^': 
        return 1
    return 0
  
def applyOp(a, b, op): 
      
    if op == '&':
        o=a[1]*b[1]
        z=4-o
        return [z,o]
    if op == '|':
        o=a[1]*b[1] + a[0]*b[1] + a[1]*b[0]
        z=4-o
        return [z,o]
    if op == '^':
        o=a[1]*b[0] + a[0]*b[1]
        z=4-o
        return [z,o]

  
def evaluate(tokens): 
      
    values = [] 
      
    ops = [] 
    i = 0
      
    while i < len(tokens): 
          
        if tokens[i] == ' ': 
            i += 1
            continue
          
        elif tokens[i] == '(': 
            ops.append(tokens[i]) 
          
        elif type(tokens[i]) is list: 
              
            values.append(tokens[i]) 
          
        elif tokens[i] == ')': 
          
            while len(ops) != 0 and ops[-1] != '(': 
              
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.pop() 
          
        else: 
          
            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                          
                val2 = values.pop() 
                val1 = values.pop() 
                op = ops.pop() 
                  
                values.append(applyOp(val1, val2, op)) 
              
            ops.append(tokens[i]) 
          
        i += 1
      
    while len(ops) != 0: 
          
        val2 = values.pop() 
        val1 = values.pop() 
        op = ops.pop() 
        #print(val1,val2,op)
                  
        values.append(applyOp(val1, val2, op)) 
    return values 



m=998244353
t=int(input())
while t:
    t-=1
    s=input()
    new=[]
    unknown=0
    for i in s:
        if i=='#':
            new.append([1,1])
            unknown+=1
        else:
            new.append(i)
    # print(new)
    
    ans=(evaluate(new))

    b=ans[0][1]
    a=pow(2,unknown)-b
    c=a*b
    d=c
    print(a,b,c,d)

    q=pow(4**unknown,m-2,m)

    print((a*a*q)%m,(b*b*q)%m,(c*q)%m,(c*q)%m)

      
