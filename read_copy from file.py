#Program to copy content of  a file to another function

import time

def delay_message(msg):
    for letter in msg:
        print(letter,end='')
        time.sleep(0.02)

def read_d(x):
    try:
        with open(x,'r') as p:
            line=p.read()
        return line
    except:
        return ('File not found')
        
def append_d(r,destination):
    with open(destination,'a') as k:
        line=k.write(r)
    delay_message('/////////////////// File successfully appended //////////////////')
    
def write_d(w,destination):
    with open(destination,'w') as f:
        line=f.write(w+'\n')
    delay_message('***********File succesfully save!************')

while True:
    menu='\n\n***************************** Menu******************************\n'
    menu+='\t\t1. Read\n\t\t2. Write\n\t\t3. Append\n\t\t4. Exit\n\t\tEnter your choice : '
    delay_message(menu)
    ch=input()
    if ch=='1':
        delay_message("Enter the name of the source file : ")
        sf=input()
        str=read_d(sf)
        delay_message(str)
    elif ch=='2':
        delay_message("Enter the name of the source file : ")
        sf=input()
        delay_message("Enter the name of the destination file : ")
        df=input()
        str=read_d(sf)
        write_d(str,df)
    elif ch=='3':
        delay_message("Enter the name of the source file : ")
        sf=input()
        delay_message("Enter the name of the destination file : ")
        df=input()
        str1=read_d(sf)
        append_d(str1,df)
    elif ch=='4':
        delay_message("!!!!!!!!!!!!!!!!!!!! :) Thank You :) !!!!!!!!!!!!!!!!!!!")
        break
    else:
        delay_message('############### Invalid Choice, Try Again ###############')
        continue




    

    
