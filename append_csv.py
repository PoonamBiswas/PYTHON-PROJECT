import csv

def open_read_csv():
    with open('member1.csv','r') as d:
       c=csv.reader(d)
       for line in c:
           for word in line:
               print(word,end='\t')
           print()
open_read_csv()

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

#---------------------------------------------------------------------------------
            
def open_append_csv():
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
                continue
            elif choice=='n' or choice=='N':
                break

#------------------------------------------------------------------------------

def open_modify_csv():
    with open('member1.csv','r+',newline='') as d:
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
            else:
                v.append(line)
            print()
        w=csv.writer(d,delimiter=',')
        w.writerows(v)
        
            
#---------------------------

def open_delete_csv():
    with open('member1.csv','r+',newline='') as d:
        c=csv.reader(d,delimiter=',')
        v=[]
        for line in c:
            for word in line:
                print(word,end='\t')
            print()
            ch=input('Delete(y/n)? : ')
            if ch in ('Y','y'):
                continue
            else:
                v.append(line)
            print()

