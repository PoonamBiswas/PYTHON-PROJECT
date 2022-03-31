#Program to search names in dat file

import diamond_collection as dc

while True:
    print('\nChoices :')
    print('\n\t>>Modify(M)\n\t>>Delete(D)\n\t>>View(V)\n\t>>Write(W)\n\t>>Append(A)\n\t>>Exit(E)')
    c=input('\n  What is your choice : ')
    print()
    if c in ('M','m'):
        dc.open_modify()
    elif c in ('D','d'):
        dc.open_delete()
    elif c in ('V','v'):
        dc.open_read()
    elif c in ('W','w'):
        dc.open_write()
    elif c in ('A','a'):
        dc.open_append()
    elif c in ('E','e'):
        break
    else:
        print('!!!!!!!!!! Invalid Call, Try again !!!!!!!!')
        continue

   
