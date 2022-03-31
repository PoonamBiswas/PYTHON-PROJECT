#dat file showing employee detail lesser than Rs 12000

import csv

with open('emp_detail1.dat','r') as d:
    text=csv.reader(d)
    ct=0
    r=[]
    flag=0
    s=int(input('Enter salary limit : Rs '))
    for line in text:
        if ct==0:
            a=['=================================================']
            r.append(line)
            r.append(a)
        else:
            if int(line[3])<s:
                flag+=1
                r.append(line)
        ct-=1
    if flag!=0:
        for line in r:
            for word in line:
                print('{:22}'.format(word),end='')      
            print()
    else:
        print('There is no employee with a salary below Rs',s)
        
