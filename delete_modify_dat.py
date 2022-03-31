#Program to search names in dat file

import pickle

ctd=0
ctm=0
file_flag=False
flag=False
new_list=[]
try:
    with open('member.dat','rb+') as d:
        print('Your records are :\n')
        file_flag=True
        while True:
            text=pickle.load(d)
            for line in text:
                print(line,end='\t')
            c=input('\nModify(M) or Delete(D)? ')
            print()
            if c in ('M','m'):
                ctm+=1
                flag=True
                no=input('\tChanged Mno. : ')
                mn=input('\tChanged Mname : ')
                new_list.append([no,mn])
                print()
            elif c in ('D','d'):
                ctd+=1
                flag=True
            else:
                new_list.append(text)
        if ctm==1:
            l='record'
        else:
            l='records'
        if ctd==1:
            o='record'
        else:
            o='records'

except:
    if flag==True:
        with open('member.dat','wb+') as d:
            for record in new_list:
                pickle.dump(record,d)
        print('\n',ctm,l,'modified successfully')
        print('\n',ctd,o,'deleted successfully')
        
    elif file_flag==False:
        print('File not found')

