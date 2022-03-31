#program to enter a dictionary of emp records in binary csv file

import pickle

def emp_dict():
    with open('employee.dat','wb') as f:
        while True:
            ecode=input('  Empcode : ')
            ename=input('  Empname : ')
            desig=input('  Designation : ')
            sal=int(input('  Salary : '))
            rec={'Emp code':ecode,'Emp name':ename,'Designation':desig,'Salary':sal}
            pickle.dump(rec,f)
            while True:
                c=input('\n  Do you want to continue(y/n)? ')
                if c in 'ynYN':
                    break
                else:
                    print('\n--------------!!!!!!!!!!!!!! Invalid Choice !!!!!!!!!!!!!!-----------\n')
            if c in 'nN':
                break

with open('employee.dat','rb') as r:
    ct=0
    while True:
        try:
            a=pickle.load(r)
            if a['Salary']>5000 and a['Designation']=='Cleck':
                ct+=1
                print(a)
        except:
            break
            
    print('\nNo. of emp salary greater than 5000 are',ct)
