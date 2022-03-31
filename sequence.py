#Program to make sequence

def sequence(a,b,c):
    r=[]
    for i in range(a,b,c):
        r.append(i)
    return r

e=int(input('Enter the starting value : '))
f=int(input('Enter the ending value : '))
g=int(input("Enter the steps : "))
x=sequence(e,f,g)
print('The list of the sequence is\n',x)
