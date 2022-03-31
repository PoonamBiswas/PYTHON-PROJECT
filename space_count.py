#Program to count no. of spaces in a file

def count_space(filename):
    with open(filename,'r') as k:
        m=k.read()
        ct=m.count(' ')
    print('Number of spaces in the file is ',ct)

a=input('Enter the source file : ')
count_space(a)
