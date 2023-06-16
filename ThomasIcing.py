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

#srchstr = "C:\\Users\\mysti\\Desktop\\AutoProd\\Raw"

srchstr = 'E:\\Acid_Loops\\'

#contentbeats = []
contentdrones = []
#contentperc = []
contentpepper = []
#contentbass = []
#contentorg = []
#contentsax = []
contentgit = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav")  and  ("Tabla" in str(filepath))  : 

            #contentsax.append(filepath) 

            contentdrones.append(filepath)

            #contentpepper.append(filepath)

            contentgit.append(filepath)

        if  filepath.endswith(".wav")  and  ("Thomas_Singing_Bowls" in str(filepath))  :   

            contentpepper.append(filepath)

        #if  filepath.endswith(".wav")  and  ("Urban_Sounds_Saint_Louis_01242023" in str(filepath)) and  ("LouPercSess" in str(filepath))  :     

            #contentperc.append(filepath)

            #contentbeats.append(filepath)

        #if  filepath.endswith(".wav")  and  ("Bass" in str(filepath)) and ("Industrial" in str(filepath)) and (("Drum" not in str(filepath)) and ("Beat" not in str(filepath)))  :

            #ontentbass.append(filepath)   

        #if  filepath.endswith(".wav")  and ("Beat" in str(filepath)) and ("Dub" in str(filepath)) and  ("Bass" not in str(filepath)) :

            #contentbeats.append(filepath)
             

        #if  filepath.endswith(".wav")  and ("Ukelele" in str(filepath))   : 

            #contentgit.append(filepath)

        #if  filepath.endswith(".wav")  and ("WorldEthnic" in str(filepath))  : 
             
            #contentpepper.append(filepath)

        #if  filepath.endswith(".wav")  and ("Deep" in str(filepath)) and ("Drone" in str(filepath))   : 

            #contentdrones.append(filepath)

        #if  filepath.endswith(".wav")  and (("Key" in str(filepath)) or ("Vo" in str(filepath))) and ("Glitch" in str(filepath))   : 

            #contentorg.append(filepath) 

        #if  filepath.endswith(".wav")  and ("Bass" in str(filepath)) and  ("Trip" in str(filepath)): 

            #contentbass.append(filepath)            

        #if  filepath.endswith(".wav")  and (("Beat" in str(filepath)) or ("Drum" in str(filepath))) and ("Trip" in str(filepath)) :     
                   
            #contentbeats.append(filepath)
            
        #if  filepath.endswith(".wav")  and ("Perc" in str(filepath)) and ("Glitch" in str(filepath))   : 

            #contentperc.append(filepath)

print("")

print("Gathering Root Sounds.")

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

call(["python", "DJProcessorIcing.py"])

## THE GHOST OF THE SHADOW ##
