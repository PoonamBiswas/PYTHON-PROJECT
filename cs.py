def ATOEDISP():
    with open('NEWS.txt', 'r') as f:
        data = f.read()
        word= data.split(' ')
        s=''
        for letter in word:
            if 'COMPUTAR' in letter:
                s+=letter.replace('A', 'E')
            else:
                s+=letter

    return s
print(ATOEDISP())
