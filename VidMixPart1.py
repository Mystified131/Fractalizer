#This code imports the necessary modules.

#from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

#srchstr = "C:\\Users\\mysti\\Desktop\\PianoWarp"

#srchstr= 'C:\\Users\\mysti\\Desktop\\LouPerc_01232023'

#srchstr = "F:\\Acid_Loops\\"

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

orgvid = []

srchstr = "C:\\Users\\mysti\\Desktop\\AutoProd\\SourceVideos\\"

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
         
        if  filepath.endswith(".mp4")    : 

            orgvid.append(filepath)

totvid = len(orgvid)

for cr in range(totvid):

    vidin = orgvid[cr]

    print("")

    print("Copying Video " + str(cr + 1) + " to work zone.")

    print("")

    newf =  "C:\\Users\\mysti\\Coding\\Fractalizer\\" + "WorkingVidSource_" + tim + "_" + str(cr) + ".mp4"
    shutil.copy(vidin, newf)

call(["python", "VidMixPart2.py"])

## THE GHOST OF THE SHADOW ##
