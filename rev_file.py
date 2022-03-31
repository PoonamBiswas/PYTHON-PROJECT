

def rev_file(flnm):
    with open(flnm,'r') as d:
        line=d.readlines()
        for i in line:
            print(i[::-1],end=' ')


a=input('Source file : ')
rev_file(a)
