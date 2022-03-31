#Program to print 3-character word

def three_ch(flnm):
    with open(flnm,'r') as r:
        line=r.read()
        ct=0
        for w in line.split():
            if len(w)==3:
                ct+=1
                print(w)
        print('No. of word containing 3 letters = ',ct)
three_ch('palindrome.py')
