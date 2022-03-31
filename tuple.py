#Program to count no. of positive, negative and zero


def calculation(n1,n2):
    ctp,ctz,ctn=0,0,0
    for i in range(n1,n2+1):
        if i==0:
            ctz+=1
        elif i>0:
            ctp+=1
        elif i<0:
            ctn+=1
    print(ctp,ctz,ctn)

a=int(input('Enter the starting value : '))
b=int(input('Enter the ending value : '))
calculation(a,b)
