#Program to find Palindrome of number

def palindrome (n):
    r=0
    m=n
    while n>0:
        d=n%10
        r=r*10+d
        n=n//10
    if r==m:
        print(m,' is palindrome .')
    else:
        print(m,' is not palindrome .')
    
a=int(input('Enter the number : '))
palindrome (a)
