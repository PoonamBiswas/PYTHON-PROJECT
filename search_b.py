import pickle

try:
    with open('emp_detail.dat','rb') as d:
        n=str(input('Name : '))
        flag=False
        while flag==False:
            lists=pickle.load(d)
            for line in lists:
                if line==n:
                    flag=True
                    print(lists)
                    break
except:
    if flag==False:
            print('\t!!!!!!!!!! Not Found!!!!!!!!!')
