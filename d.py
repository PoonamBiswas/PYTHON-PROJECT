import csv
def open_search_csv():
    flag=0
    with open('member1.csv','r') as d:
        a=csv.reader(d)
        x=input('Mno(M) or Name(N) : ')
        for line in a:
            if x in line:
                print()
                for word in line:
                    print(word,end='\t')
                flag=1
                print()
    if flag==0:
        print('\nRecord not found')

        
open_search_csv()
            
        
