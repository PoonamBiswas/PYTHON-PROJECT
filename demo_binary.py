#Binary file in csv to read and write

import pickle

def pickle_write():
    with open('First.txt','wb') as f:
        pickle.dump([12,'King'],f)

def pickle_read():
    with open('First.txt','rb') as f:
        a=pickle.load(f)
        print(a)

pickle_read()
