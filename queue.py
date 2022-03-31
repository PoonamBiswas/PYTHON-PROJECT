#program to implement queue using list (FIFO)

list1=[]
while True:
    print('\n  Menu for queue :')
    ch=input('\n\t>> Insert(I)\n\t>> Pop(P)\n\t>> Display(D)\n\t>> Any to Exit\n\n\t>> Enter your choice :  ')
    if ch in 'Ii':
        while True:
            i=int(input('\n  Insert here : '))
            list1.append(i)
            c=input('  Do you want to insert more(y/n)? ')
            if c in 'yY':
                continue
            else:
                break
    elif ch in 'pP':
        if len(list1)==0:
            print('\n  No element to pop.')
        else:
            print(list1.pop(0),' has been succesfully popped from the list.')
            
    elif ch in 'Dd':
        if len(list1)==0:
            print('  No element to display.')
        else:
            print('The queue elements are :',list1)
    else:
        print('\n  !! Thank You :) !!')
        break

