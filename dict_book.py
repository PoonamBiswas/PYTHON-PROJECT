

import pickle

with open('Book_dict.dat','ab+') as d:
    a=int(input('How many records you want to enter : '))
    for i in range(0,a):
        bno=input('\nEnter Book no. : ')
        bname=input('Enter Book name : ')
        author=input('Enter Author\'s name : ')
        price=float(input('Enter Book price : '))
        dict={'Book No.':bno,'Book Name':bname,'Author':author,'Price':price}
        pickle.dump(dict,d)
    print()
    d.seek(0)
    ct=0
    while True:
        try:
            a=pickle.load(d)
            if a['Book Name'].lower()=='python':
                ct+=1
                if ct==1:
                    print('Book No.','B Name','Author','Price\n',sep='\t')
                print(a['Book No.'],a['Book Name'],a['Author'],a['Price'],sep='\t')
        except:
            break
