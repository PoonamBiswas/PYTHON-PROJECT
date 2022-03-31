#Program to find the sum and difference consecutively upto a number

def sd(n):
    s=0
    d=0
    for i in range(1,n+1):
        if i%2!=0:
            s+=i  
        else:
            d+=i
    k=s-d
    return k

a=int(input("Enter the number : "))
l=sd(a)
print("The result will be ",l)            
            
