#Program to swap

def swap(l):
    for i in range(0,len(l)-1,2):
        l[i],l[i+1]=l[i+1],l[i]
    return l

print(swap([12,23,34,45,56,6,778,89,90]))
        
