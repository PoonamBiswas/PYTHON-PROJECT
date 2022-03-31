#Program to search name whose salary is less than 4000

import csv

def sname():
    with open('sname_emp.csv','r') as r:
        text=csv.reader(r)
        ct=0
        rec=[]
        flag=False
        for line in text:
            if int(line[2])<4000:
                ct+=1
                rec.append(line)
                flag=True
        if flag==False:
            print('No employee whose salary is less than 4000.')
        else:
            for line in rec:
                for word in line:
                    print(word,end='\t')
                print()
            print('\nNo. of employee whose salary is lesser than 4000 are : ',ct)

sname()
