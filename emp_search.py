#Program to search employee details

import csv

def search_detail(desg,sal):
    with open('emp_detail.csv','r',newline='') as g:
        text=csv.reader(g)
        flag=False
        ct=0
        title=[]
        for line in text:
            ct+=1
            if ct==1:
                title.append(line)
            if line[2]==desg and int(line[3])<sal:
                flag=True
                title.append(line)
        if flag==False:
            print('No such employee exist')
        else:
            for line in title:
                for word in line:
                    print(word,end='\t')
                print()


desg=input('Enter Designation : ')
sal=int(input('Enter Salary Limit : '))
search_detail(desg,sal)
                
        
