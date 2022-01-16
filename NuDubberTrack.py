#This code imports the necessary modules.

import random
import os
from pydub import AudioSegment
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from pydub.utils import make_chunks
import numpy as np
import math
from subprocess import call
import shutil

def reduce_volume(atrack, trvol):

    stsound = -22

    if trvol < stsound:
        chvol = (stsound - trvol)
        atrack = atrack + chvol

    if trvol > stsound:
        chvol = (trvol - stsound)
        atrack = atrack - chvol

    return atrack

def bass_line_freq(track):
    #sample_track = list(track)

    # c-value
    est_mean = np.mean(track)

    # a-value
    est_std = 3 * np.std(track) / (math.sqrt(2))

    bass_factor = int(round((est_std - est_mean) * 0.005))

    return bass_factor

def get_loudness(sound, slice_size):
    return max(chunk.dBFS for chunk in make_chunks(sound, slice_size))


right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

outfile = open('AutoPlayListBeats.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsamplebeat" in str(filepath) :
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()

outfile = open('AutoPlayListDrones.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsampledrone" in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()


outfile = open('AutoPlayListPepper.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsamplepepper" in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()


outfile = open('AutoPlayListGit.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "guitar" in str(filepath)  and "newsound" not in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()

infile = open("AutoPlayListBeats.m3u", "r")

contentbeats = []

plist = infile.readline()
while plist:
    contentbeats.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListDrones.m3u", "r")

contentdrones = []

plist = infile.readline()
while plist:
    contentdrones.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListPepper.m3u", "r")

contentpepper = []

plist = infile.readline()
while plist:
    contentpepper.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListGit.m3u", "r")

contentgit = []

plist = infile.readline()
while plist:
    contentgit.append(plist)
    plist = infile.readline()
infile.close()

trtot = 18

suctot = 0

for ctr in range(700):

    try:

        atracknum1 = random_number2(0,len(contentbeats))
        atrack1 = contentbeats[atracknum1].strip()

        newAudiobeat = AudioSegment.from_wav(atrack1) 

        #######

        #atracknum1 = random_number2(0,len(contentbeats))
        #atrack1 = contentbeats[atracknum1].strip()
        atracknum2 = random_number2(0,len(contentgit))
        atrack2 = contentgit[atracknum2].strip()
        atracknum3 = random_number2(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random_number2(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random_number2(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random_number2(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random_number2(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random_number2(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random_number2(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random_number2(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random_number2(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random_number2(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random_number2(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random_number2(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random_number2(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random_number2(0,len(contentpepper))

        print("")

        print("Layering tracks for track: ", (suctot + 1))


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

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudioambq1 = newAudioamb2 * 2

        if len(newAudiobeat) >= len(newAudioambq1):

            newAudionear1 = newAudioambq1.overlay(newAudiobeat)
        
        if len(newAudiobeat) < len(newAudioambq1):

            newAudionear1 = newAudiobeat.overlay(newAudioambq1)

        
        atracknum1 = random_number2(0,len(contentbeats))
        atrack1 = contentbeats[atracknum1].strip()

        newAudiobeat = AudioSegment.from_wav(atrack1) 

        #######

        #atracknum1 = random_number2(0,len(contentbeats))
        #atrack1 = contentbeats[atracknum1].strip()
        atracknum2 = random_number2(0,len(contentgit))
        atrack2 = contentgit[atracknum2].strip()
        atracknum3 = random_number2(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random_number2(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random_number2(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random_number2(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random_number2(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random_number2(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random_number2(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random_number2(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random_number2(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random_number2(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random_number2(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random_number2(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random_number2(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random_number2(0,len(contentpepper))

        print("")

        print("Layering tracks for track: ", (suctot + 1))


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

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudioambq2 = newAudioamb2 * 2

        if len(newAudiobeat) >= len(newAudioambq2):

            newAudionear2 = newAudioambq2.overlay(newAudiobeat)
        
        if len(newAudiobeat) < len(newAudioambq2):

            newAudionear2 = newAudiobeat.overlay(newAudioambq2)

        #######

        #atracknum1 = random_number2(0,len(contentbeats))
        #atrack1 = contentbeats[atracknum1].strip()
        atracknum2 = random_number2(0,len(contentgit))
        atrack2 = contentgit[atracknum2].strip()
        atracknum3 = random_number2(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random_number2(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random_number2(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random_number2(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random_number2(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random_number2(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random_number2(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random_number2(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random_number2(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random_number2(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random_number2(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random_number2(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random_number2(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random_number2(0,len(contentpepper))

        print("")

        print("Layering tracks for track: ", (suctot + 1))


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

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudioambq3 = newAudioamb2 * 2

        if len(newAudiobeat) >= len(newAudioambq3):

            newAudionear3 = newAudioambq3.overlay(newAudiobeat)
        
        if len(newAudiobeat) < len(newAudioambq3):

            newAudionear3= newAudiobeat.overlay(newAudioambq3)

        newAudionear = newAudionear1 + newAudionear2 + newAudionear3 + newAudionear3 
            
        attenuate_db = 0
        accentuate_db = .24
        goldsound = -18
        stsound = -23

        leng = len(newAudionear)

        startvol = get_loudness(newAudionear, leng)

        if startvol < -16 and startvol > -18.5:

            newAudio2 = reduce_volume(newAudionear, startvol)

            filtered = newAudio2.low_pass_filter(bass_line_freq(newAudio2.get_array_of_samples()))

            newAudio3 = (newAudio2 - attenuate_db).overlay(filtered + accentuate_db)

            loudn = get_loudness(newAudio3, leng)

            print(loudn)

            if loudn <= goldsound:
                chvol = (goldsound - loudn)
                newAudio3 = newAudio3 + chvol

            if loudn > goldsound:
                chvol = (loudn - goldsound)
                newAudio3 = newAudio3 - chvol

            prod = int(360000 / (len(newAudio3)))

            rep2 = prod - 3

            newAudio4 = newAudio3 * rep2

            newAudio4 = newAudio4.fade_in(9000)

            newAudio4 = newAudio4.fade_out(9000)

            oufil = "C:\\Users\\mysti\\Desktop\\AutoProd\\Raw\\Mastered_Track" + tim + "." + str(suctot) + ".wav"
            newAudio4.export(oufil, format="wav")

            suctot += 1

            if suctot == trtot:
                break

    except:

        print("")

        print("Error during render. File not created.")

call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\StartTrackEvolvingHere.py"])

## THE GHOST OF THE SHADOW ##
