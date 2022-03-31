#Program to print words ending with 'o' in a file

def word(flnm):
    with open(flnm,'r') as r:
        line=r.readlines()
        for w in line:
            for j in w.split():
                if j[-1]=='o':
                    print(j)
word('just_for_fun.txt')
