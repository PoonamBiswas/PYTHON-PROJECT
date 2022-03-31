#Function to copy content of  a file to another function

import time
import pickle

def delay_message(msg):
    for letter in msg:
        print(letter,end='')
        time.sleep(0.02)

def read_d(x):
    with open(x,'r') as p:
        line=p.read()
    return line

def append_d(r,destination):
    with open(destination,'a') as k:
        line=k.write(r)
    delay_message('/////////////////// File successfully appended //////////////////')
    
def write_d(w,destination):
    with open(destination,'w') as f:
        line=f.write(w+'\n')
    delay_message('***********File succesfully save!************')

#Function to find the factorial

def factorial(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s


#Function to find the sum of all inverse

def inverse_sum(n):
    r=0
    for i in range(1,n+1):
        d=1/i
        r+=d
    return r


#Function to find the sum of all digits in a number

def sum_of_digits(n):
    r=0
    while n>0:
        d=n%10
        r+=d
        n=n//10
    return r


#Function to print Fibonacci uptill a no.

def fibonacci(n):
    l=[]
    a=0
    b=1
    if n==1:
        l.append(a)
        return l
    elif n==2:
        l.append(a)
        l.append(b)
        return l
    else:
        l.append(a)
        l.append(b)
        for i in range(3,n+1):
            c=a+b
            l.append(c)
            a=b
            b=c
        return l

        
#Function to find Palindrome of number

def palindrome(n):
    r=0
    m=n
    while n>0:
        d=n%10
        r=r*10+d
        n=n//10
    if m==r:
        return 1
    else:
        return 0
          
    

#Function to check prime number

def isprime(n):
    if n<2:
        return 0
    ct=0
    for i in range(2,n):
        if n%i==0:
            ct+=1
    if ct==0:
        return 1
    else:
        return 0


#Function to check Armstrong of a number

def isarmstrong(n):
    r=0
    m=n
    while n>0:
        d=n%10
        r+=d**3
        n=n//10
    if m==r:
        return 1
    else:
        return 0


#Function to find the sum and difference consecutively upto a number

def sum_difference(n):
    s=0
    d=0
    for i in range(1,n+1):
        if i%2!=0:
            s+=i  
        else:
            d+=i
    k=s-d
    return k

#Function to find the sum of inverse of factorial

def inverse_factorial(n):
    r=0
    for i in range(1,n+1):
        r+=1/(factorial(i))
    return r


#Function to open write mode in binary csv

def open_write():
    with open('member.dat','wb') as j:
        while True:
            a=input('\n\tMno. : ')
            b=input('\tEmp. name : ')

            #b=input('\tDesignation : ')
            #c=int(input('\tSalary : '))
            pickle.dump([a,b],j)
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

#Function to open append mode in binary csv

def open_append():
    with open('member.dat','ab') as j:
        while True:
            a=input('\n\tMno. : ')
            b=input('\tEmp. name : ')

            #b=input('\tDesignation : ')
            #c=int(input('\tSalary : '))
            pickle.dump([a,b],j)
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


#CSV binary read

def open_read():
    with open('member.dat','rb') as r:
        while True:
            try:
                a=pickle.load(r)
                for line in a:
                    print(line,end='\t')
                print()
            except:
                break


#Function to delete binary dat file

def open_delete():
    ct=0
    file_flag=False
    flag=False
    new_list=[]
    try:
        with open('member.dat','rb+') as d:
            file_flag=True
            while True:
                text=pickle.load(d)
                for line in text:
                    print(line,end='\t')
                c=input('\nDelete(Y/N)? ')
                print()
                if c in ('Y','y'):
                    ct+=1
                    flag=True
                else:
                    new_list.append(text)
                
    except:
        if flag==True:
            with open('member.dat','wb+') as d:
                for record in new_list:
                    pickle.dump(record,d)
            print('\n',ct,'record deleted successfully')
        elif file_flag==False:
            print('File not found')

#Function to modity dat binary file

def open_modify():        
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

#Function to write in csv file
            
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
