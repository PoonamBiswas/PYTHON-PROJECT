#Program to print words ending with 't' in a file

def word(flnm):
    with open(flnm,'r') as r:
        line=r.readlines()
        ct=0
        for w in line:
            for j in w.split():
                if j[0] in 'tT':
                    ct+=1
                    print(j)
        print('No. of words = ',ct)
word('just_for_fun.txt')
