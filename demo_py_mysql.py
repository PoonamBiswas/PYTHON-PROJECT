import mysql.connector as mc

mydb=mc.connect(host='localhost',user='root',password='',database='diamond')
mycursor=mydb.cursor()

def search(name):
    query_s="select * from teacher where Name=%s;"
    rec=(name,)
    res=mycursor.execute(query_s,rec)
    mycursor.fetchall()
    return int(mycursor.rowcount)
    

def insert():
    ct=0
    while True:
        name=input('\nTeacher name : ')
        subject=input('Subject : ')
        sal=int(input('Salary : '))
        doj=input('Date of Joining(YYYY-MM-DD) : ')
        query='insert into teacher values(%s,%s,%s,%s)'
        rec=(name,subject,sal,doj)
        mycursor.execute(query,rec)
        mydb.commit()
        ct+=mycursor.rowcount
        while True:
            ch=input('\nDo you want to continue(y/n)? ')
            if ch in 'YynN':
                break
            else:
                print('\n  Invalid Choice')
        if ch in 'Yy':
            continue
        else:
            break
    if ct>0:
        print(ct,'records inserted succesfully.')
    else:
        print('No record inserted.')

def copy():
    query="select * from teacher;"
    mycursor.execute(query)
    result=mycursor.fetchall()
    ct=0
    for tuple in result:
        query_copy='insert into profession values(%s,%s,%s,%s)'
        rec=(tuple[0],tuple[1],tuple[2],tuple[3])
        mycursor.execute(query_copy,rec)
        mydb.commit()
        ct+=1
    print(ct,'record(s) copied to PROFESSION table succcesfully')
        
def display():
    print()
    print(' The records present in TEACHER table are : \n')
    query="select * from teacher;"
    mycursor.execute(query)
    result=mycursor.fetchall()
    for tuple in result:
        for word in tuple:
            print(word,end='')
            if len(str(word))<10:
                a=15-len(str(word))
                print(' '*a,end='')
        print()

def update():
    ct=0
    while True:
        name=input('\nTeacher name : ')
        if search(name)==0:
            print('\nTeacher not found')
            ch=input('\nDo you want to continue(y/n)? ')
            if ch in 'Yy':
                continue
            else:
                break
            
        nname=input('Input new teacher name : ')
        nsubject=input('New Subject : ')
        nsal=int(input(' New Salary : '))
        ndoj=input(' New Date of Joining(YYYY-MM-DD) : ')
        query="update teacher set name=%s, subject=%s, salary=%s, DOJ=%s where name =%s"
        rec=(nname,nsubject,nsal,ndoj,name)
        mycursor.execute(query,rec)
        mydb.commit()
        ct+=mycursor.rowcount
        
        while True:
            ch=input('\nDo you want to continue(y/n)? ')
            if ch in 'YynN':
                break
            else:
                print('\n  Invalid Choice')
        if ch in 'Yy':
            continue
        else:
            break
    if ct>0:
        print(ct,'record(s) updated succesfully.')
    else:
        print('No record updated.')
        

def delete():
    name=input('Name to be deleted : ')
    query="delete from teacher where Name=%s;"
    rec=(name,)
    mycursor.execute(query,rec)
    mydb.commit()
    if mycursor.rowcount>0:
        print(mycursor.rowcount,'records deleted succesfully.')
    else:
        print('No record(s) found.')

def salary(sal):
    query='select * from teacher where salary<=%s;'
    rec=(sal,)
    mycursor.execute(query,rec)
    dis=mycursor.fetchall()
    for i in dis:
        for x in i:
            print(x,end='      ')
        print()

while True:
    ch=input('\n  Menu\n\ti) Display(D)\n\tii) Insert(I)\n\tiii) Update(U)\n\tiv) Delete(P)\n\tv) Search(S)\n\tvi) Copy(C)\n\tvii) Salary limit(L)\n\tviii) Exit(any)\n\t   Enter your choice : ')
    if ch in 'Dd':
        display()
    elif ch in 'Ii':
        insert()
    elif ch in 'Uu':
        update()
    elif ch in 'Pp':
        delete()
    elif ch in 'Ss':
        name=input('\nName to be searched : ')
        c=search(name)
        print(c,'record(s) found.')
    elif ch in 'Cc':
        copy()
    elif ch in 'Ll':
        sal=int(input('Salary limit : '))
        salary(sal)
    else:
        break
    print('\n---------------------------------------------------------------------------------------------------\n')
print('\n\nTHANK YOU\n')
