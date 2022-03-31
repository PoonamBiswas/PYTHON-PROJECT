#Program to change the case of words

def case_change(flnm):
    with open(flnm,'r') as r:
        line=r.read()
        for ch in line:
            if ch.islower():
                print(ch.upper(),end='')
            elif ch.isupper():
                print(ch.lower(),end='')
            else:
                print(ch,end='')

case_change('just_for_fun.txt')
