#Program to chech scholars

import csv

def scholar():
    with open('scholar.csv','r') as t:
        text=csv.reader(t)
        for line in text:
            if int(line[1])>75:
                for word in line:
                    print('{:10}'.format(word),end='')
                print()

scholar()
