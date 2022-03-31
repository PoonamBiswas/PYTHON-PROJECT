#program to implement stack - push(), pop() and display() (LIFO)

book=[]

def push_book():
    a=input('Book no. : ')
    b=input('Book name : ')
    book.append([a,b])
    print('Pushed succesfull\n')
    while True:
        c=input('Do you want to push more(y/n)? ')
        if c in 'yYnN':
            break
        else:
            print('Invalid choice')
    if c in 'yY':
        push_book()
        
def pop_book():
    if len(book)==0:
        print('\nCannot pop. Stack is empty.\n')
    else:
        book.pop()
        print('Poped succesfull\n')
    
def display_book():
    if len(book)==0:
        print('\nStack is empty.\n')
    else:
        print('The current stack of book details :\n')
        for line in book:
            for word in line:
                print(word,end='\t')
            print()
    print()
while True:
    print('  Choice : ')
    print('\n\t>> Push(A)\n\t>> Pop(P)\n\t>> Display(D)\n\t>> Exit(E)')
    ch=input('\n  Enter your choice : ')
    if ch in ('A','a'):
        push_book()
    elif ch in ('P','p'):
        pop_book()
    elif ch in ('D','d'):
        display_book()
    else:
        break
