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


srchstr = "F:\\OriginalAudio\\Songs"

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

print("")

print("Please wait while the processor applies organic logic to your track collection.")

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        modtim = os.path.getmtime(filepath)

        sz = os.path.getsize(filepath)

        if  (sz > 80000000) and filepath.endswith(".wav") and ("And" not in str(filepath)) and ("With" not in str(filepath)) and ("Generated" not in str(filepath)) and ("Oriondrive" not in str(filepath))and ("Futurelight" not in str(filepath)) and ("FutureLight" not in str(filepath)) and (modtim > 1218050000):

                content.append(str(filepath))

contentb = []

srchstrb = "C:\\Users\\mysti\\Media_Files\\Sounds\\HomemadeSamplesReadyToMix"

for subdir, dirs, files in os.walk(srchstrb):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav"):

                contentb.append(str(filepath))

cotr = random_number2(3, 6)

tots = random_number(len(contentb))

for x2 in range(cotr):
    xx = random_number(tots)
    atr = contentb[xx]
    outstr = "C:\\Users\\mysti\\Coding\\Fractalizer\\GeneFX" + str(time) + "_" + str(x2 + 1) +  ".wav"
    shutil.copy(atr, outstr)
    print("")
    print("Copying: " + str(x2))
    print("")
   
clen = len(content)

for ctr in range(totrk):

    xin = random_number(clen)
    fortrk = content[xin]
    outstr = "C:\\Users\\mysti\\Coding\\Fractalizer\\Imported_" + str(time) + "_" + str(ctr + 1) +  ".wav"
    shutil.copy( fortrk, outstr)
    print("")
    print("Copying: " + str(ctr+1))
    #outlst.append(sttrk)
    #newply.remove(newply[valu])

print("")

#srchstr2 = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\"

#contentloc = []

#for subdir, dirs, files in os.walk(srchstr2):
    #for file in files:
        #filepath = subdir + os.sep + file

        #if  filepath.endswith(".wav") :

            #cstr = str(filepath)
            #contentloc.append(cstr)

#ounam = "DreamFrogOrderedPlaylist_" + time + ".m3u"

#outfile = open(ounam, "w")

#for elem in finlst:
     #outfile.write(elem + '\n')

#outfile.close() 

#ounm = "DreamFrogOrderedTracklist_" + time + ".txt"

#outfile = open(ounm, "w")

#for elem in outlst:
     #outfile.write(elem + '\n')

#outfile.close() 

#ounm2 = "DreamFrogOrderedLocalPlaylist_" + time + ".m3u"

#outfile = open(ounm2, "w")

#for elem in contentloc:
     #outfile.write(elem + '\n')

#outfile.close() 

print("")

print("The tracks have been copied into the local folder.")

print("")

call(["python", "SpeakInParagraphsWorldFact.py"])

## THE GHOST OF THE SHADOW ##
