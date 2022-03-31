with open('palindrome.py') as f:
    line=f.readlines()
    for i in line:
        for j in i.split():
            print(j)
