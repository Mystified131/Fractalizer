#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from pathlib import Path
import shutil
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call
     

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))

#print("")

#totrk = int(input("How many tracks would you like to add to this playlist? The minimum is 5 and the default is 50: "))

#if not totrk:
totrk = 25 #This variable controls length of output playlist

#if totrk <= 4:
    #totrk = 5

#print("")

#cpy = str(input ("Would you like to copy these files to the static folder? To copy is the default. If so, please press 'Y': "))

#if not cpy:
#cpy = "Y" #This variable controls whether we copy the files to the static folder

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"


srchstr = "H:\\Spirit_Circuits"

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

print("")

print("Please wait while the files are copied")

content = []
contentb = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith('.wav'):

            content.append(str(filepath))
            contentb.append(str(file))

conlen = len(content)

print(contentb)

for x in conlen:

    inpth = content[x]
    instr = contentb[x]

    ostr = "H:\\WAVDump\\" + instr

    shutil.copy(inpth, ostr)

    print("")
    print("Copying: " + str(x+ 1)) + "out of " + str(x) + " total files."
    print("")

print("Finished copying. Files in target folder.")

