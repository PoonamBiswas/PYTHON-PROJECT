#Program to write records to a csv file

import csv

def write_csv():
    with open('CSV1.csv','w') as c:
        writer=csv.writer(c,delimiter=',')
        lis=[1,2,3,4,5,'Mumbai']
        lis2=[9,6,4,1,6,'Kolkata']
        lis3=[5,2,7,4,8,'Chennai']
        writer.writerow(lis)
        writer.writerow(lis2)
        writer.writerow(lis3)

write_csv()
