import pickle

with open('VEHICAL.dat','ab+') as d:
    a=int(input('How many records you want to enter : '))
    for i in range(0,a):
        vno=input('\nEnter Vehicle code : ')
        vname=input('Enter Vehicle name : ')
        cost=float(input('Enter Vehicle cost : '))
        dict={'Vehicle Code':vno,'Vehicle name':vname,'Vehicle cost':cost}
        pickle.dump(dict,d)
    print()
    d.seek(0)
    with open('vehi.dat','wb') as f:
        while True:
            try:
                a=pickle.load(d)
                if a['Vehicle name'].lower()=='wagon r' and a['Vehicle cost']>600000:
                    pickle.dump(a,f)
            except:
                break
