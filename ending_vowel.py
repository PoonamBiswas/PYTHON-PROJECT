#Program to count words ending with vowel in a file

def word_v(flnm):
    with open(flnm,'r') as r:
        line=r.readlines()
        ct=0
        for w in line:
            for j in w.split():
                if j[-1] in 'aeiou':
                    ct+=1
                    print(j)
        print('No. of words ending with vowel are ',ct)
word_v('just_for_fun.txt')
