import csv

def open_read_csv():
    with open('member1.csv','r') as d:
       c=csv.reader(d)
       for line in c:
           for word in line:
               print(word,end='\t')
           print()

open_read_csv()
