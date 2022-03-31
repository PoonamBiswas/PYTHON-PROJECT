#Program to find the total, avg and pc of a given list of mark

def average(list):
    l=len(list)
    total=0
    for i in range(0,l):
        total+=list[i]
    avg=total/l
    pc=(total/(40*l))*100
    print('Total mark = ',total,'\n
          Percentage mark = ',pc,'\nAverage mark = ',avg)

a=[12,23,34,40,32,21]
average(a)
