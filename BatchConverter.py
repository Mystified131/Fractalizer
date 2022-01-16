#This code imports the necessary modules

import os
import re
import collections
import operator
from subprocess import call
import subprocess
import pydub

 
srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\NewerOther\\MattFPoems7282019"

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav")):
            wav = str(filepath)
            print("")
            print(wav)
            print("")

            newp = filepath[-3:0] + "mp3"

            sound = pydub.AudioSegment.from_wav(wav)
            sound.export(newp, format="mp3")   
    

import pydub
sound = pydub.AudioSegment.from_wav("D:/example/apple.wav")
sound.export("D:/example/apple.mp3", format="mp3")        

print("")

print("The designated files have been removed. Thank you.")

print("")

#call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\RadThomas.py"])

## THE GHOST OF THE SHADOW ##