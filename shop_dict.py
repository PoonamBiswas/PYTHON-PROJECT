

import pickle

def shop_dict():
    with open('SHOP.dat','ab+') as f:
        while True:
            a=input('\nShop name : ')
            b=input('Address : ')
            c=int(input('Sales : '))
            dict={'Shop name':a,'Address':b,'Sales':c}
            pickle.dump(dict,f)
            while True:
                ch=input('\nDo you want to continue(y/n)? ')
                if ch in 'YNyn':
                    break
                else:
                    print('!!!!!!! Invalid Choice !!!!!!!!')
            if ch in 'Yy':
                continue
            elif ch in 'Nn':
                break
        f.seek(0)
        a=pickle.load(f)
        min=a['Sales']
        res=a
        while True:
            try:
                a=pickle.load(f)
                if a['Sales']<min:
                    min=a['Sales']
                    res=a
            except:
                break
        print('\nThe shope that have the least sales : \n')
        print('S name\tAddress\tSales')
        print(res['Shop name'],res['Address'],res['Sales'],sep='\t')
    
                
    
shop_dict()
