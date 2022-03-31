#Program to convert seconds to hour and minute

def sec(n):
    h=n//3600
    m=n%3600
    m1=m//60
    
    s1=m%60
    print(n,' seconds = ',h,'hours ',m1,'min ',s1,'second!!!!')

a=int(input('Enter the seconds : '))

sec(a)
