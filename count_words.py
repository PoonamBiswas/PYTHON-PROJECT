#Program to find the occurance of words


import diamond_collection as dc
    
def count_word(flnm,key):
    try:
        with open(flnm,'r') as g:
            line=g.read()
            ct=0
            for w in line.split():
                if key in w:
                    ct+=1
        return ct
    except:
        print('\nERROR!!!!! ',flnm,' is not found.\n')
        return 0

dc.delay_message('\t\tThis is a program to search a word from a given file\n')
dc.delay_message('\tEnter the source file : ')
a=input()
#dc.delay_message('\tEnter the word to be searched : ')
#b=input()
c=count_word(a,'me') + count_word(a,'my')
dc.delay_message('\nThe word me/my occur '+str(c)+' times')

