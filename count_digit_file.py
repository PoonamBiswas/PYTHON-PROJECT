#Program to count digits

def ct_digit(flnm):
    with open(flnm,'r') as f:
        line=f.read()
        ct=0
        for ch in line:
            if ch in '0123456789':
                ct+=1
        print('No. of digits is ',ct)

#a=input('Enter the source file : ')
#ct_digit(a)

def ct_alpha(flnm):
    with open(flnm,'r') as f:
        line=f.read()
        ct=0
        cu=0
        for ch in line:
            if 'a'<=ch and ch<='z':
                ct+=1
            elif 'A'<=ch and ch<='Z':
                cu+=1
        print('No. of Upper case is ',cu)
        print('No. of Lower case is ',ct)

a=input('Enter the source file : ')
ct_alpha(a)
