import csv

flnm=input('Enter a source file : ')
try:
    with open(flnm,'r') as r:
        text=csv.reader(r,delimiter=',')
        for line in text:
            for word in line:
                print(word,end='\t')
            print()
except:
    print('File ',flnm,' doesn\'t exist.')
##
##flnm=input('Enter a file to create : ')
##with open(flnm,'w',newline='') as r:
##    text=csv.writer(r,delimiter=',')
##    while True:
##        line=input('Enter line : ')
##        text.writerow([line])
##        if line=='':
##            break
##
##flnm=input('Enter a destination file : ')
##with open(flnm,'a',newline='') as r:
##    text=csv.writer(r,delimiter=',')
##    while True:
##        line=input('Enter line : ')
##        text.writerow([line])
##        if line=='':
##            break
