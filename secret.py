#code
import pickle

with open('msg.txt','r') as a:
    b=a.read()
    c=b[::-1]
    with open('secret.dat','wb') as d:
        for letters in c:
            pickle.dump(letters,d)
res=''
with open('secret.dat','rb') as f:
    while True:
        try:
            a=pickle.load(f)
            res+=a
        except:
            break
print(res[::-1])
