#Program to print 4-character word

def four_ch(flnm):
    with open(flnm,'r') as r:
        line=r.read()
        ct=0
        for w in line.split():
            if len(w)==4:
                ct+=1
                print(w)
        print('No. of word = ',ct)
four_ch('palindrome.py')
