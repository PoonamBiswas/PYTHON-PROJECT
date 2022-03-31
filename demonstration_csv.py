#Program to read record from csv file

import csv

with open('record.csv','r') as s:
    reader=csv.reader(s,delimiter=',')
    c=open('CSV2.csv','w',newline='')
    writer=csv.writer(c,delimiter=',')
    ct=1
    print('\n\t\t---------------------------Menu-----------------------\n')
    print('\t\t1. For reading\n\t\t2. For writing')
    ch=input('\n\t\tEnter your choice : ')
    if ch=='1':
        for line in reader:
            for word in line:
                print(word,end='\t')
            print()
            if ct==1:
                print('=====================================================')
            ct+=1
    elif ch=='2':
        for line in reader:
            writer.writerow(line)
        print('\n\t\t=============File Wrote===========')

    else:
        print("\n\t!!!!!ERROR!!!!!! Invalid Choice!")

    c.close()
