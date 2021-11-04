import os
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime
from subprocess import call
import shutil

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

print("")

print("Generating Liner Notes. . .")

print("")

titls = []

infile = open("Titles.txt", "r")

aline = infile.readline()  

while aline:
    try:
        titls.append(aline.strip())
        aline = infile.readline()
    except: 
        print("Text error-- passing over line.")

infile.close()

titstr = ""

xt = random_number(len(titls))

titstr = titls[xt]

infile = open("RevText.m3u", "r")

revt = ""

aline = infile.readline()  

while aline:
    try:
        revt += aline.strip()
        aline = infile.readline()
    except: 
        print("Text error-- passing over line.")

infile.close()

infile = open("CapsText.m3u", "r")

kwird = []

aline = infile.readline()  

while aline:
    try:
        kwird.append(aline.strip())
        aline = infile.readline()
    except: 
        print("Text error-- passing over line.")

infile.close()

klen = len(kwird)

senlst = revt.split(".")

texlen = random_number2(8, 32)

senlen = len(senlst)

fintxt = ""

for ctr in range(texlen):
    senc = random_number(senlen)
    elem = senlst[senc]
    elem += ". "
    fintxt += elem

subl = fintxt.split(' ')

for elem in subl:
    if elem == "":
        subl.remove(elem)

mainstr = ""

for elem in subl:

    try:
        if elem[0].isupper():
            kch = random_number(klen)
            kwo = kwird[kch]
            mainstr += kwo + " "

        if not elem[0].isupper():
            mainstr += elem + " "

    except:
        print("String Error. Passing.")

a = random_number2(1, 13)
b = random_number2(1, 29)
c = random_number2(1958, 2021)

dtstr = str(a) + "/" + str(b) + "/" + str(c)

mainstr += ". -- Richard Flash, " + dtstr + " --Rolling Rock Reviews"

aulst = ["DJ_Iterate", "DJ Frankenstone", "Thomas Park"]

anum = random_number(len(aulst))

austr = aulst[anum]

anum2 = random_number(len(aulst))

aucvr = aulst[anum2]

print("")

print(mainstr)

oustr = "G:\\Spirit_Circuits\\NewAlbum\\ZZ_Liner_Notes_" + str(tim) + ".txt"

outfile = open(oustr, "w")

outfile.write("Liner Notes For: " + titstr + '\n')

outfile.write('\n')

outfile.write("This Release Was Created By "+ austr + " in the early 21st Century")

outfile.write('\n')

outfile.write("Original Cover Art By: "+ aucvr + '\n')

outfile.write('\n')

outfile.write(mainstr + '\n')

outfile.write('\n')

outfile.write("The artist's homepage is: https:\\archive.org\\details\\ThomasParkBenchmarkHub" + '\n')

outfile.write('\n')

outfile.write("Please release as a cc non-commercial or public domain license." + '\n')

outfile.write('\n')

outfile.close()       

print("")

print("Your document is saved in the same folder as this code.")

print("")

instr = "G:\\Spirit_Circuits\\NewAlbum"
#instr = "C:\\Users\\mysti\\Desktop\\NewAlbum"

outstr = "G:\\Spirit_Circuits\\" + titstr
#outstr = "C:\\Users\\mysti\\Desktop\\" + titstr

try:

    os.rename(instr, outstr)

except:

    print("")

    print("Unable to rename directory.")

print("")

print("Your project should be ready for you in the AutoProd folder on your desktop and a folder in the Spirit Circuits folder on your Seagate external drive.")

print("")

movlst = []

for subdir, dirs, files in os.walk("C:\\Users\\mysti\\Desktop\\AutoProd\\Raw"):
    for file in files:
        filepath = subdir + os.sep + file

        if ".wav" in str(filepath):
            movlst.append(filepath)

for elem in movlst: 

    try:

        #shutil.copy(elem, "C:\\Users\\mysti\\Desktop\\AutoProd\\Older_Mastered")
        #print("Copying Track.")
        #print("")
        os.remove(elem)

    except:

        print("Copying error. . .")
        print("")

call(["python",  "C:\\Users\\mysti\\Coding\\Fractalizer\\BatchDeleter.py"])

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

    





