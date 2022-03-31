a#CSV binary append

import pickle

with open('Ham.txt','ab') as r:
    while True:
        a=input('\n\tName : ')
        b=input('\tPhone : ')
        pickle.dump([a,b],r)
        choice=input('\n\tEnter \'y\' to continue or else will break : ')
        if choice in ['Y','y']:
            continue
        else:
            break
            
    
