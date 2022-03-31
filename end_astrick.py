#Program to terminate output with a *


def end_astrick(x):
    with open(x,'r') as f:
        line=f.read()
        for i in line.split():
            print(i,end='*')

a=input('Enter the source file  : ')
end_astrick(a)
        
