

import pickle

with open('Book.dat','rb+') as d:
    a=int(input('How many records you want to enter : '))
    for i in range(0,a):
        bno=input('\nEnter Book no. : ')
        bname=input('Enter Book name : ')
        author=input('Enter Author\'s name : ')
        price=float(input('Enter Book price : '))
        list=[bno,bname,author,price]
        pickle.dump(list,d)
    d.seek(0)
    while True:
        try:
            a=pickle.load(d)
            if a[1].lower()=='python':
                for word in a:
                    print(word,end='\t')
                print()
        except:
            break
