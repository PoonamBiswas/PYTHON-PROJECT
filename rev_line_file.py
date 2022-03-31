#Program to show the reverse line in a file

def rev_line(flnm):
    try:
        with open(flnm,'r') as y:
            line=y.readlines()
            for i in line[::-1]:
                print(i)
    except:
        print('!!!!!!!ERROR!!!!!!! File not found!')
a=input('Enter the source file : ')
rev_line(a)
