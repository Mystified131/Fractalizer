import os
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime
from subprocess import call
from TextGetter import GetWebTextSF

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

print("")

print("Generating Possiblities. . .")

print("")

kwird = GetWebTextSF()

outlist = []

for elem in kwird:
    oustr = elem.title() + " Hyperion", "Hyperion " + elem.title()
    outlist.append(oustr)

print(outlist)

oustr = "C:\\Users\\mysti\\Coding\\Fractalizer\\Permutation_" + str(tim) + ".txt"

outfile = open(oustr, "w")

for elem2 in outlist:

    for elem3 in elem2:

        outfile.write(elem3 + '\n')

outfile.close()       

print("")

print("Your document is saved in the same folder as this code.")

print("")

#call(["python", "AlbumNamer.py"])

## THE GHOST OF THE SHADOW ##






    #subl = elem.split(' ')
    #totl = len(subl)
    #for x2 in range(totl):
        #astr = subl[x2]
        #if astr[0].isupper():
            #kch = random_number(klen)
            #kwo = kwird[kch]
            #subl[x2] = kwo
        #print(subl)

    





