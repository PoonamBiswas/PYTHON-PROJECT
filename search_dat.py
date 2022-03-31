#Program to modify names in dat file

import pickle

ct=0
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
            c=input('\nModify(Y/N)? ')
            print()
            if c in ('Y','y'):
                ct+=1
                flag=True
                no=input('\tChanged Mno. : ')
                mn=input('\tChanged Mname : ')
                new_list.append([no,mn])
                print()
            else:
                new_list.append(text)
            
except:
    if flag==True:
        with open('member.dat','wb+') as d:
            for record in new_list:
                pickle.dump(record,d)
        print('\n',ct,'record updated successfully')
    elif file_flag==False:
        print('File not found')

