#Program to

def skip_word(flnm,flnm2):
    with open(flnm,'r') as d:
        line=d.read()
        with open(flnm2,'w') as f:
            for i in line.split():
                if i[0] in 'AEIOU':
                    pass
                else:
                    f.write(i+' ')
        

skip_word('Textfile.txt','Textfile2.txt')
