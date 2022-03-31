#sum of digits using recursion

def sum_recur(a):
    if a==0:
        return 0
    else:
        return a%10+sum_recur(a//10)

a=int(input('Enter a no. : '))
print(sum_recur(a))
