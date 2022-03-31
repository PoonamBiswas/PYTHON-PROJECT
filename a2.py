def fibonacci(m):
    l=[]
    a=0
    b=1
    if m==0:
        l.append(a)
        return l
    elif m==1:
        l.append(a)
        l.append(b)
    else:
        l.append(a)
        l.append(b)
        for i in range(3,m):
            c=a+b
            l.append(c)
            a=b
            b=c
        return l

a=20
print(fibonacci(a))
            
