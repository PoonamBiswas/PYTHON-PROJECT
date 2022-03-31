#Program to check Armstrong of a number

def armstrong(n):
    r=0
    while n>0:
        d=n%10
        r+=d**3
        n=n//10
    return r

a=int(input("Enter a number to check Armstrong : "))

t=armstrong(a)

if a==t:
    print("The number ",a," is Armstrong")
else:
    print("Not Armstrong")
