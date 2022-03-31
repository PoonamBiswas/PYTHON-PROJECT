#CSV binary read

import pickle

with open('member.dat','rb') as r:
    while True:
        try:
            a=pickle.load(r)
            for line in a:
                print(line,end='\t')
            print()
        except:
            break
    
