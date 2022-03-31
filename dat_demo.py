#showing employee's salary less than 20000

with open('emp_detail1.dat','r') as i:
    a=i.readlines()
    print(a)
    ct=1
    for line in a:
        if ct==1:
            pass
        else:
            b=0
            for word in line:
                if b==3:
                    print(word,end='')
                b+=1
        ct+=1

        
        
    
