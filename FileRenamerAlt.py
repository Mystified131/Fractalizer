#This code imports the necessary modules

import os
import re
import collections
import operator
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call
from TextGetter import GetWebText

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))


#rootdir = "C:\\Users\\mysti\\Desktop\\NewAlbum"

#rootdir = "C:\\Users\\mysti\\Desktop\\NewBad10.13.2021"

#rootdir = "C:\\Users\\mysti\\Coding\\Fractalizer"

rootdir = 'C:\\Users\\mysti\\Coding\\Fractalizer'

filtyp = ".wav"

print("")

print("Renaming files . . This may take a moment. . .")

print("")

#rootnam = input("Please enter a root string to use as the new filename basis: ")

#print("")

if filtyp == "All":

    fillst = []
    fillrt = []
    filltyp = []

    for subdir, dirs, files in os.walk(rootdir):

        for file in files:
            filepath = subdir + os.sep + file
            froot = subdir + os.sep 
            fstr = str(file)
           
            nummer = fstr.rindex(".")
            
            fstr2 = fstr[nummer:]
            fillst.append(str(filepath))
            fillrt.append(str(froot))
            filltyp.append(str(fstr2))


if filtyp != "All":

    fillst = []
    fillrt = []
    filltyp = []

    for subdir, dirs, files in os.walk(rootdir):

        for file in files:
            filepath = subdir + os.sep + file
            froot = subdir + os.sep 
            if filepath.endswith(filtyp):
                fillst.append(str(filepath))
                fillrt.append(str(froot))
                filltyp.append(filtyp)

lx = len(fillst)

#srchstr = "C:\\Users\\mysti\\Desktop\\NewAlbum"

srchstr = "C:\\Users\\mysti\\Desktop\\Nimmo"

wordcon = GetWebText()

x1 = len(wordcon)

phraselist = []

for phrs in range(lx):

    for wiz in range(3):
        num1 = random_number(x1)
        num2 = random_number(x1) 
        num3 = random_number(x1) 
        astr = wordcon[num1]
        bstr = wordcon[num2]
        cstr = wordcon[num3]
        phrsstr = astr + "_" + bstr + "_" + cstr
        phraselist.append(phrsstr)


for ctr in range(lx):

    astr = fillst[ctr]
    bstr =  fillrt[ctr] + phraselist[ctr] + filltyp[ctr] 

    os.rename(astr, bstr) 

print("")

print("The chosen files have been renamed. Thank you.")

print("")

#call(["python", "CoverArt.py"])

## THE GHOST OF THE SHADOW ##