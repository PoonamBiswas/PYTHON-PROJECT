#Program for searching in csv file

import csv

def search_name(name):
    with open('marksheet.csv','r') as c:
        text=csv.reader(c)
        ct=0
        flag=False
        for line in text:
            ct+=1
            if ct==1:
                title=line
            if line[0]==name:
                flag=True
                for i in title:
                    print(i,end='\t')
                print()
                for word in line:
                    print(word,end='\t')
        if flag==False:
            print('Record not found')

name=input('Enter name to be searched : ')
search_name(name)
