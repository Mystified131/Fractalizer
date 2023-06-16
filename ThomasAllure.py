#This code imports the necessary modules.

from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

#srchstr = "C:\\Users\\mysti\\Desktop\\PianoWarp"

#srchstr= 'C:\\Users\\mysti\\Desktop\\LouPerc_01232023'

srchstr = "F:\\Acid_Loops\\pocket"

contentbeats = []
contentdrones = []
contentperc = []
contentpepper = []
contentbass = []
contentorg = []
contentsax = []
contentgit = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
         
        #if  filepath.endswith(".wav")  and ("Space" in str(filepath)): 

            #contentdrones.append(filepath)

            #contentorg.append(filepath) 

        #if  filepath.endswith(".wav")  and   ("Sci" in str(filepath)) :

            #contentsax.append(filepath) 

            #contentpepper.append(filepath)

            #contentgit.append(filepath)

        #if  filepath.endswith(".wav")  and  ("Pad" in str(filepath)  and  "Space" in str(filepath)):
            #contentperc.append(filepath)

        #if  filepath.endswith(".wav")  and  ("String" in str(filepath)  and  "Space" in str(filepath)) :     

            #contentbeats.append(filepath)

        #if  filepath.endswith(".wav")  and  ("Drone" in str(filepath)) and  ("Bass" in str(filepath)):

            #contentbass.append(filepath)   

        #if  filepath.endswith(".wav")  and ("Beat" in str(filepath)) and ("Dub" in str(filepath)) and  ("Bass" not in str(filepath)) :

            #contentbeats.append(filepath)

    
        if  filepath.endswith(".wav")   : 

            contentsax.append(filepath)             

        if  filepath.endswith(".wav")   : 

            contentgit.append(filepath)

        if  filepath.endswith(".wav")   : 
             
            contentpepper.append(filepath)

        if  filepath.endswith(".wav")   : 

            contentdrones.append(filepath)

        if  filepath.endswith(".wav")   : 

            contentorg.append(filepath) 

        if  filepath.endswith(".wav")   : 

            contentbass.append(filepath)            

        if  filepath.endswith(".wav")  and ("mallet" in str(filepath)) :     
                   
            contentbeats.append(filepath)
            
        if  filepath.endswith(".wav")   : 

            contentperc.append(filepath)


print("")

print("Gathering Root Sounds.")

x = len(contentbeats)

for ctr in range(80):
    y = random_number(x)
    atrack = contentbeats[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundbeat' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbeats[y], outstr)

x = len(contentdrones)

for ctr in range(120):
    y = random_number(x)
    atrack = contentdrones[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsounddrone' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentdrones[y], outstr)

x = len(contentperc)

for ctr in range(120):
    y = random_number(x)
    atrack = contentperc[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundperc' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentperc[y], outstr)

x = len(contentpepper)

for ctr in range(150):
    y = random_number(x)
    atrack = contentpepper[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundpepper' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentpepper[y], outstr)

x = len(contentbass)

for ctr in range(50):
    y = random_number(x)
    atrack = contentbass[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundbass' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbass[y], outstr)

x = len(contentorg)

for ctr in range(100):
    y = random_number(x)
    atrack = contentorg[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundgorgan' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentorg[y], outstr)

x = len(contentsax)

for ctr in range(100):
    y = random_number(x)
    atrack = contentsax[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundsaxophone' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentsax[y], outstr)

x = len(contentgit)

for ctr in range(100):
    y = random_number(x)
    atrack = contentgit[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\newsoundguitar' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentgit[y], outstr)

call(["python", "DJProcessorPlanker.py"])

## THE GHOST OF THE SHADOW ##
