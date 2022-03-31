#Program to show the reverse in a list

def reverse_list(l):
    r=l[::-1]
    return r

a=list(input("Enter a list : "))
b=reverse_list(a)
print(b)
