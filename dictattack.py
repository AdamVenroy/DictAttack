import os
import sys
dictlist = []
chosendict = []
numrange = 9999
pick = None
n = 0
password = 'twgrwgwe'
dir_path = os.path.dirname(os.path.realpath(__file__))
for i in os.listdir(dir_path + '/dictionaries'):
    if i.endswith('.txt'):
        dictlist.append(i)

print('Pick Dictionaries (Numerically):')
for i in dictlist: 
    print('[%s]%s' % (n, i))
    n += 1

while pick != '':
    pick = input()
    if pick != '':
        chosendict.append(dictlist[int(pick)])
        print('Chosen Dicts: ' + str(chosendict))

for d in chosendict:
    dictfile = open('%s\dictionaries\%s' % (dir_path, d), 'r', encoding='ISO-8859-1')
    for line in dictfile:
        word = line.strip()
        print(word)
        if word == password:
            print('password is: %s' % word)
            exit()
        elif word.upper() == password:
            print('password is: %s' % word.upper())
        else:
            for n in range(0, numrange):
                wordnum = word + str(n)
                # print(wordnum)
                if wordnum == password:
                    print('password is: %s' % wordnum)
                    exit()



    dictfile.close()


