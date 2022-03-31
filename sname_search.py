#Program to search name staarting with S

import csv

def sname():
    with open('sname_emp.csv','r') as r:
        text=csv.reader(r)
        ct=0
        rec=[]
        flag=False
        for line in text:
            #for word in line:
            if line[1][0]=='S':
                ct+=1
                rec.append(line)
                flag=True
        if flag==False:
            print('No employee starting with \'S\' exist.')
        else:
            for line in rec:
                for word in line:
                    print(word,end='\t\t')
                print()
            print('No. of employee starting with \'S\' are : ',ct)

sname()
