#program to perform read, write, update, append, delete in csv file

import csv

def open_view_csv():
    with open('member1.csv','r') as d:
       c=csv.reader(d)
       for line in c:
           for word in line:
               print(word,end='\t')
           print()
    print()

#----------------------------------------------------------------------------------
           
def open_write_csv():
    with open('member1.csv','w',newline='') as j:
        c=csv.writer(j,delimiter=',')
        while True:
            a=input('\n\tMno. : ')
            b=input('\tEmp. name : ')
            c.writerow([a,b])
            while True:
                choice=input('\n\tDo you want to continue? (y/n) : ')
                if choice in ('y','Y','n','N'):
                    break
                else:
                    print('\n\t\t!!!!!!! Invalid call !!!!!!!!\n\n')
            print()
            if choice=='y' or choice=='Y':
                continue
            elif choice=='n' or choice=='N':
                break
    print()


#---------------------------------------------------------------------------------
            
def open_append_csv():
    ct=1
    with open('member1.csv','a',newline='') as j:
        c=csv.writer(j,delimiter=',')
        while True:
            a=input('\n\tMno. : ')
            b=input('\tEmp. name : ')
            c.writerow([a,b])
            while True:
                choice=input('\n\tDo you want to continue? (y/n) : ')
                if choice in ('y','Y','n','N'):
                    break
                else:
                    print('\n\t\t!!!!!!! Invalid call !!!!!!!!\n\n')
            print()
            if choice=='y' or choice=='Y':
                ct+=1
                continue
            elif choice=='n' or choice=='N':
                break
    if ct==1:
        r='record'
    else:
        r='records'
    print('\n\t',ct,r,'appended')
    print()


#------------------------------------------------------------------------------

def open_modify_csv():
    ct=0
    with open('member1.csv','r') as d:
        c=csv.reader(d,delimiter=',')
        v=[]
        for line in c:
            for word in line:
                print(word,end='\t')
            print()
            ch=input('Modify(y/n)? : ')
            if ch in ('Y','y'):
                a=input('\n\tMno. : ')
                b=input('\tEmp. name : ')
                v.append([a,b])
                ct+=1
            else:
                v.append(line)
            print()
    with open('member1.csv','w',newline='')  as l:  
        w=csv.writer(l,delimiter=',')
        w.writerows(v)
    if ct==1:
        r='record'
    else:
        r='records'
    print('\n\t',ct,r,'modified')
    print()
        
            
#----------------------------------------------------------------------------

def open_search_csv():
    flag=0
    with open('member1.csv','r') as d:
        a=csv.reader(d)
        x=input('Mno(M) or Name(N) : ')
        for line in a:
            if x in line:
                print()
                for word in line:
                    print(word,end='\t')
                flag=1
                print()
    if flag==0:
        print('\nRecord not found')
    print()

#---------------------------------------------------------------------------------

def open_delete_csv():
    ct=0
    with open('member1.csv','r+',newline='') as d:
        c=csv.reader(d,delimiter=',')
        v=[]
        for line in c:
            for word in line:
                print(word,end='\t')
            print()
            ch=input('Delete(y/n)? : ')
            if ch in ('Y','y'):
                ct+=1
            else:
                v.append(line)
            print('\n')
    with open('member1.csv','w',newline='')  as l:  
        w=csv.writer(l,delimiter=',')
        w.writerows(v)
    if ct==1:
        r='record'
    else:
        r='records'
    print('\t',ct,r,'deleted')
    print()

#------------------------------------Function definitions end here--------------------------------------

while True:
    print('\nChoices :')
    print('\n\t>> View(V)\n\t>> Modify(M)\n\t>> Search(S)\n\t>> Delete(D)\n\t>> Create New/Write(W)\n\t>> Append(A)\n\t>> Exit(E)')
    c=input('\n  What is your choice : ')
    print()
    if c in ('M','m'):
        open_modify_csv()
    elif c in ('D','d'):
        open_delete_csv()
    elif c in ('V','v'):
        open_view_csv()
    elif c in ('W','w'):
        open_write_csv()
    elif c in ('A','a'):
        open_append_csv()
    elif c in ('S','s'):
        open_search_csv()
    elif c in ('E','e'):
        break
    else:
        print('!!!!!!!!!! Invalid Call, Try again !!!!!!!!')
        continue

