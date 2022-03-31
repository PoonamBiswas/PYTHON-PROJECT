#Program to Print student of sec A rec

import csv

def student_rec(sec):
    with open('student_rec.csv','r',newline='') as r:
        text=csv.reader(r)
        ct=0
        title=[]
        i=sec.upper()
        flag=0
        for line in text:
            ct+=1
            if ct==1:
                title.append(line)
            if line[0]==i:
                flag=1
                title.append(line)
        if flag==0:
            print('Entered SEC not found')
        else:
            for line in title:
                for word in line:
                    print(word,end='\t\t')
                print()

sec=input('Enter the sec. : ')
student_rec(sec)
