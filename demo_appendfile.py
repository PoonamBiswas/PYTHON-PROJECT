#Program to demonstrate append mode in file

f=open('Notes.txt','a')
while True:
    line=input('Line : ')
    f.write(line+'\n')
    if (len(line))==0:
        break
f.close()
