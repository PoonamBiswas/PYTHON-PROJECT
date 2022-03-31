#Program to count words starting with 'A' or 'a' in a file

def word_v(flnm):
    with open(flnm,'r') as r:
        line=r.readlines()
        ct=0
        for w in line:
            for j in w.split():
                if j[0] in 'aA':
                    ct+=1
                    print(j)
        print('No. of words starting with \'A\' or \'a\' are ',ct)
word_v('just_for_fun.txt')
