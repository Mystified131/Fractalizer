#This code imports the necessary modules.

import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call

try:

    os.mkdir("G:\\Spirit_Circuits\\NewAlbum")

except:

    print("")

    print("Unable to create directory.")

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

contentbeats = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and "Imported" in str(filepath):
            contentbeats.append(str(file))

contentgitr = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and "Generated_voxraw" in str(filepath) or "GeneFX" in str(filepath) :
            contentgitr.append(str(file))
       
print("")

print("Preparing samples.")

print("")

contentgit = []

ctr = 1

for x3 in range(25):

    try:
        lin = len(contentgitr)
        samran = random_number(lin)
        atrack = contentgitr[samran]
        print("Sample: " + str(x3 - 25))
        print("")
        ctr += 1
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random_number(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(2000, 4000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(8,10)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(100)
            newAudio = newAudio.fade_out(100)
            sil1 = random_number2(12000, 17000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(23000, 53000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(4,7)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number2(10000, 14000)
            sil2 = random_number2(18000, 25000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 7 and solonum < 11:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(17000, 22000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(8, 11)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number2(22000, 25000)
            sil2 = random_number2(13000, 18000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 10:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(2000, 3000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(9 ,12)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            addAudio = newAudio
            ctr = random_number2(3,8)
            for sam in range(ctr):
                newAudio += addAudio
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number2(10000, 14000)
            sil2 = random_number2(13000, 17000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back

        dic = random_number(10)
        if dic == 7:
            sil1 = random_number(22000)
            sil2 = random_number(18000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
            newAUdio = newAudio - 1
        oufil = "C:\\Users\\mysti\\Coding\\Fractalizer\\vsamp" + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
        titsamp = "vsamp" + str(ctr) + ".wav"
        contentgit.append(titsamp)

    except:
        print("File unreadable.")


trtot = len(contentbeats)

for ctr in range(trtot):

    try:
        atrack1 = contentbeats[ctr]
        atracknum2 = random_number2(0,len(contentgit))
        atrack2 = contentgit[atracknum2]
        atracknum3 = random_number2(0,len(contentgit))
        atrack3 = contentgit[atracknum3]
        atracknum4 = random_number2(0,len(contentgit))
        atrack4 = contentgit[atracknum4]


        print("")

        print("Layering tracks for track: ", (ctr+ 1))


        newAudio1 = AudioSegment.from_wav(atrack2)       
        totlen = len(newAudio1)

        newAudio2 = AudioSegment.from_wav(atrack3) 
        l2 = len(newAudio2)
        rep = int(totlen / l2)

        newAudiox = newAudio2*rep

        newAudiow2 = newAudio1.overlay(newAudiox)

        newAudio3 = AudioSegment.from_wav(atrack4) 
        l2 = len(newAudio3)
        rep = int(totlen / l2)

        newAudiox = newAudio3*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudioamb1 = newAudiow3.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudioamb2 = newAudioamb2 * 8

        newAudiobeat = AudioSegment.from_wav(atrack1) 
        newvol = 2
        newAudiobeat = newAudiobeat - newvol

        if len(newAudiobeat) >= len(newAudioamb2):

            newAudionear = newAudioamb2.overlay(newAudiobeat)
        
        if len(newAudiobeat) < len(newAudioamb2):

            newAudionear = newAudiobeat.overlay(newAudioamb2)

        newAudionear = newAudionear.fade_in(5000)
        newAudionear = newAudionear.fade_out(15000)

        oufil = "G:\\Spirit_Circuits\\NewAlbum\\Track" + tim + "." + str(ctr) + ".wav"
        newAudionear.export(oufil, format="wav")

    except:

        print("")

        print("Error during render. File not created.")

call(["python", "RawTrax5.py"])

## THE GHOST OF THE SHADOW ##
