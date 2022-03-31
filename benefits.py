

def benefits(d):
    if d=='Director' or 'director':
        c='Mercedes Benz'
        h='Luxurious Flat'
    elif d=='Manager':
        c='Audi A3'
        h='Premium Flat'
    elif d=='Accountant':
        c='Maruti Suzuki Dzire'
        h='Delux Flat'
    return c,h

a=input("Enter the one following designation and know the benefits : \nDirector , Mnager , Accountant : ")
b,f=benefits(a)
print('The benefits for the designation ',a,' are ',b,' and ',f,'.')
