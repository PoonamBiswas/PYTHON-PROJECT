#Program to show the sum by using recursion

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

a=int(input('Enter a no. : '))

print('The arithmethic sum of',a,'is',sum(a))
    
