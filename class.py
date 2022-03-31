import pickle
def Writedata():
    with open("MEMBER.DAT","wb") as f:
        l=[]
        while True:
            Mno = int(input("Mno :"))
            Nam = input("Name ")
            l.append([Mno,Nam])
            choice = input("enter more (y/n): ")
            if choice in "nN":
                break
        pickle.dump(l,f)

def Readdata():
    with open("MEMBER.DAT","rb") as f:
        l=pickle.load(f)
        print("in readdata function, type of l is ",type(l))
        for i in l:
            print(type(i))
            print(i)

def AddData():
    with open("MEMBER.DAT","rb+") as f:
        l=pickle.load(f)
        while True:
            Mno = int(input("Mno :"))
            Nam = input("Name ")
            l.append([Mno,Nam])
            
            choice = input("enter more (y/n): ")
            if choice in "nN":
                break
        #print("in Adddata function ",f.tell())
        f.seek(0)
        pickle.dump(l,f)

def SearchDataMemNo():
    with open("MEMBER.DAT",'rb') as f:
        l=pickle.load(f)
        Memno=int(input("enter the member number to be searhed"))
        for i in l:
            if (i[0]==Memno):
                print(Memno, " found and name is ",i[1])
                break
        else:
            print(Memno, " not found")

def SearchDataMemName():
    with open("MEMBER.DAT",'rb') as f:
        l=pickle.load(f)
        Memname=input("enter the member name to be searhed")
        for i in l:
            if (i[1]==Memname):
                print(Memname, " found and number is ",i[0])
                break
        else:
            print(Memname, " not found")
            
        


Writedata()
Readdata()
AddData()
Readdata()
SearchDataMemNo()
SearchDataMemName()
