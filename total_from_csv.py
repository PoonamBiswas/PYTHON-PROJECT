

import csv

def read_file():
    a='marksheet.csv'
    try:
        with open(a,'r') as s:
            reader=csv.reader(s,delimiter=',')
            ct=0
            for line in reader:
                sum=0
                ct+=1
                if ct==1:
                    for word in line:
                        print(word,end='\t')
                    print('Tot\tAvg\tPC')
                    print('====================================================================================')
                    continue
                    
                for word in range(0,3):
                    print(line[word],end='\t')
                for word in range(3,len(line)):
                    sum+=int(line[word])
                    print(line[word],end='\t')
                print(sum,'\t',sum/5,'\t',(sum/250)*100) 
               
    except:
        print('\n\tThe File ',a,' does not exist.')

read_file()
