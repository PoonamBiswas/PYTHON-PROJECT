#program to perform read, write and append operation on csv file

import csv

def read_file():
    print('\n\tWE ARE IN READ FILE FUNCTION\n')
    a=input('Enter the source file you want to read from : ')
    try:
        with open(a,'r') as s:
            reader=csv.reader(s,delimiter=',')
            ct=1
            for line in reader:
                if ct==1:
                    for word in line:
                        print('{:^15}'.format(word),end='')
                    print('\n=====================================================')
                else:
                    for word in line:
                        print('{:^18}'.format(word),end='')
                    print()
                ct+=1
    except:
        print('\n\tThe File ',a,' does not exist.')

def write_file():
    print('\n\tWE ARE IN WRITE FILE FUNCTION\n')
    a=input('Enter the name of the file you want to create : ')
    with open(a,'w',newline='') as c:
        writer=csv.writer(c,delimiter=',')
        lis=[]
        while True:
            
            a=input('Name : ')
            b=input('Phone no. : ')
            lis.append([a,b])
            
            choice=input('Do you want to insert more records?(y/n) ')
            if choice=='n':
                writer.writerows(lis)
                break
        
        print('\n\t\t=============File Written Successfully===========')

def append_file():
    print('\n\tWE ARE IN APPEND FILE FUNCTION\n')
    a=input('Enter the source file you want to append in : ')
    with open(a,'a',newline='') as c:
        writer=csv.writer(c,delimiter=',')
        while True:
            lis=[]
            a=input('Name : ')
            b=input('Phone no. : ')
            lis.append(a)
            lis.append(b)
            writer.writerow(lis)
            choice=input('Do you want to insert more records?(y/n) ')
            if choice=='n':
                break
print('\t***Program to perform Read, Write and Append operation on CSV file***\n')

while True:
    print('\n\t\t---------------------------Menu-----------------------\n')
    print('\t\t1. For reading\n\t\t2. For writing\n\t\t3. For append\n\t\t4. Exit')
    ch=input('\n\t\tEnter your choice : ')
    if ch=='1':
        read_file()
    elif ch=='2':
        write_file()
    elif ch=='3':
        append_file()
    elif ch=='4':
        break
    else:
        print('\n\t\t!!!!!!ERROR!!!!!!! Invalid Choice!')
    
    
