#Program to find the sum of all digits in a number

def sum(n):
    r=0
    while n>0:
        d=n%10
        r+=d
        n=n//10
    print(r)
a=int(input("Enter a number whose you want to find the sum of their digits : "))
sum(a)
