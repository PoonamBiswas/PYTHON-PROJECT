#Program to print alternate lines

def alt_line(flnm):
    with open(flnm,'r') as r:
        line=r.readlines()
        for w in line[::2]:
            print(w,end='')
alt_line('palindrome.py')
