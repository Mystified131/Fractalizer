import os
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime
from subprocess import call

copies = 10

for cotr in range(copies):

    right_now = datetime.datetime.now().isoformat()          
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    print("")

    print("Generating Rock Text. . .")

    print("")

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

    texlen = random_number2(3, 10)

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

    oustr = "C:\\Users\\mysti\\Coding\\Fractalizer\\Liner_Notes_" + str(tim) + ".txt"

    outfile = open(oustr, "w")

    outfile.write(mainstr + '\n')

    outfile.write('\n')

    outfile.close()       

print("")

print("Your documents are saved in the same folder as this code.")

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

        





