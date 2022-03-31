#program for summing digits

n=int(input('Enter a no. : '))
g=0

while (n != 0):
    r=n%10
    g+=r
    n=n//10
    print(r)
print("The sum of digits is ",g)    

