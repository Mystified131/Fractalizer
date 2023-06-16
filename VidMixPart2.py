#This code imports the necessary modules.

from pydub import AudioSegment
import random
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2
from moviepy.editor import *
import io
import datetime
import subprocess


def VidTrim(filloc, ln):

    print("")

    print("Rendering file: ", filloc)

    print("")

    try:

        clip1 = VideoFileClip(filloc)
        len1 = clip1.duration

        lim1 = int(len1 - ln)
        if lim1 == 0:
            lim1 += 1
        lim2 = lim1 - ln

        st = random_number(lim1)
        en = st + ln

        #try:

        clip = clip1.cutout(st, en)

       # except: 

            #try:

            #clip = clip1.cutout(0, ln)

            #except:

                #size = (200, 100)
                #clip = VideoFileClip(size, ln, fps=25, color=(0,0,0))

        return clip

    except:

        print("")

        print("File cropping error.")

        print("")

        return clip1

def WaveFromMP4(fileloc):

    filot = str(fileloc)
    filot2 = filot[:-3]
    filot3 = filot2 + "wav"

    vclip = VideoFileClip(fileloc)
    clen = ((vclip.duration) * 1000)

    newsound = AudioFileClip(fileloc)
    clen = ((newsound.duration) * 1000)
    
    try:
        newsound.write_audiofile(filot3, 44100, 2, 2000,"pcm_s16le")

    except:

        silence_seg = AudioSegment.silent(duration=clen)
        silence_seg.export(filot3, format="wav")
    
def PyPlanker(newAudio):
        
        audlen = len(newAudio)

        audseg = int(audlen / 1000) 

        segnum = int(audseg * 2)

        sllen = int(20) + 7
        
        audlen = int(audlen / segnum)

        SilAudio = AudioSegment.silent(duration = sllen)

        OutAud = newAudio[0:0]

        for iter in range(segnum):

            stval = iter * audlen
            enval2 = stval + audlen
            enval = stval + (audlen - sllen)

            SlicAud = newAudio[stval:enval]

            Slic1Aud = SlicAud.fade_in(5)

            Slic2Aud = Slic1Aud.fade_out(2)

            CutAud = Slic2Aud + SilAudio

            OutAud += CutAud

        return OutAud

def add_stutter(newAudio):
    
    audlen = len(newAudio)

    slen = random_number2(1000,3000)

    slctot = (int(audlen/slen))

    slpt = 0

    altAudio = newAudio[0:0]

    for ctr in range(slctot):

        try:

            slen = random_number2(1000,3000)

            slend = slpt + slen

            altAudio = altAudio + newAudio[slpt:slend]

            sttr = random_number2(50, 225)

            sttrinc = random_number2(3, 6)

            sval = slend - sttr

            stutAud = newAudio[sval:slend]

            for ctr in range(sttrinc):

                altAudio = altAudio + stutAud

            slpt  += slen

        except:

            print("")

            print("Process Termination")

            print("")

            return altAudio

    return altAudio

def add_deelay(newAudio):
   
    audlen = len(newAudio)

    delln = random_number2(100, 800)

    delAudio = AudioSegment.silent(duration = delln)

    delitr = random_number2(4, 6)

    defad = 1 / delitr * 18

    defad2 = .4 * defad

    altAudio = newAudio - defad2

    altAudiodelt = newAudio[0:0]

    for ctr in range(delitr):

        altAudionew = delAudio + altAudio

        altAudionew = altAudionew - defad

        altAudio = altAudio + delAudio

        altAudiodelt = altAudionew.overlay(altAudio)

        altAudio = altAudiodelt - defad2

    return newAudio

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

outfile = open('AutoPlayListBeats.m3u', "w")

contentsvid = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp4") : 
            contentsvid.append(filepath)
            WaveFromMP4(filepath)

print("Extracting samples. Please wait.")

print("")

sizlim = 15000000

for ctr in range(50):

    astr = ("Beat Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentsvid))
    avidtrack = contentsvid[songch]
    trackname = avidtrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    atrack = avidtrack[0:-4] + ".wav"

    bstr = ("Bass Sample: " + str(ctr + 1))
    print(bstr)
        
    songchb = random_number2(0,len(contentsvid))
    bvidtrack = contentsvid[songchb]
    btrack = bvidtrack[0:-4] + ".wav"

    cstr = ("Organ Sample: " + str(ctr + 1))
    print(cstr)
        
    songchc = random_number2(0,len(contentsvid))
    cvidtrack = contentsvid[songchc]    
    ctrack = cvidtrack[0:-4] + ".wav"  

    cstr = ("Organ Sample 2: " + str(ctr + 1))
    print(cstr)
        
    songchc = random_number2(0,len(contentsvid))
    cvidtrack2 = contentsvid[songchc]    
    ctrack2 = cvidtrack2[0:-4] + ".wav"  

    dstr = ("Stab Sample: " + str(ctr + 1))
    print(dstr)
        
    songchd = random_number2(0,len(contentsvid))
    dvidtrack = contentsvid[songchd]   

    dtrack = dvidtrack[0:-4] + ".wav"

    estr = ("Perc Sample: " + str(ctr + 1))
    print(estr)
        
    songche = random_number2(0,len(contentsvid))
    evidtrack = contentsvid[songche]   

    etrack = evidtrack[0:-4] + ".wav"

    estr = ("Perc Sample 2: " + str(ctr + 1))
    print(estr)
        
    songche = random_number2(0,len(contentsvid))
    evidtrack2 = contentsvid[songche]   
    etrack2 = evidtrack2[0:-4] + ".wav"

    fstr = ("Perc Sample 3: " + str(ctr + 1))
    print(fstr)
        
    songchf = random_number2(0,len(contentsvid))
    fvidtrack = contentsvid[songchf] 
    ftrack = fvidtrack[0:-4] + ".wav"

    fstr = ("Perc Sample 4: " + str(ctr + 1))
    print(fstr)
        
    songchf = random_number2(0,len(contentsvid))
    fvidtrack2 = contentsvid[songchf] 
    ftrack2 = fvidtrack2[0:-4] + ".wav"

    #try:

    newAudio = AudioSegment.from_wav(atrack)

    newAudio = newAudio - 2
            

    newAudiob = AudioSegment.from_wav(btrack)

    newAudiob = newAudiob - 2

    newAudiob = newAudiob * 4
    

    newAudioc = AudioSegment.from_wav(ctrack)
    
    newvolc = random_number2(12,15)
    newAudioc = newAudioc - newvolc


    newAudioc2 = AudioSegment.from_wav(ctrack2)
    
    newvolc = random_number2(12,15)
    newAudioc2 = newAudioc2 - newvolc

    newAudioc2 = newAudioc2 * 2

    newAudiod = AudioSegment.from_wav(dtrack)

    newvold = random_number2(12,18)
    newAudiod = newAudiod - newvold

    
    newAudioe = AudioSegment.from_wav(etrack)
    
    newvole = random_number2(10,12)
    newAudioe = newAudioe - newvole

    newAudioe = newAudioe * 4
    

    newAudioe2 = AudioSegment.from_wav(etrack2)
    
    newvole = random_number2(10,12)
    newAudioe2 = newAudioe2 - newvole

    newAudioe2 = newAudioe2 * 2


    newAudiof = AudioSegment.from_wav(ftrack)
    
    newvolf = random_number2(12, 14)
    newAudiof = newAudiof - newvolf
    
    newAudiof2 = AudioSegment.from_wav(ftrack2)
    
    newvolf = random_number2(12, 14)
    newAudiof2 = newAudiof2 - newvolf
    
    newAudiof2 = newAudiof2 * 4

    newAudio1 = newAudiof2.overlay(newAudiof)
    newAudioVidlen = int(len(newAudio1)/1000)
    newAudioVid1 = VidTrim(fvidtrack, newAudioVidlen)
    
    oufilv1 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeatvid1" + tracknam + str(ctr) + ".mp4"
    newAudioVid1.write_videofile(oufilv1)

    newAudio2 = newAudioe2.overlay(newAudio1)
    newAudio2Vidlen = int(len(newAudio2)/1000)
    newAudioVid2 = VidTrim(evidtrack2, newAudio2Vidlen)

    oufilv2 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeatvid2" + tracknam + str(ctr) + ".mp4"
    newAudioVid2.write_videofile(oufilv2)

    newAudio3 = newAudioe.overlay(newAudio2)
    newAudio3Vidlen = int(len(newAudio3)/1000)
    newAudioVid3 = VidTrim(evidtrack, newAudio3Vidlen)

    oufilv3 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeatvid3" + tracknam + str(ctr) + ".mp4"
    newAudioVid3.write_videofile(oufilv3)

    newAudio4 = newAudiod.overlay(newAudio3)
    newAudio4Vidlen = int(len(newAudio4)/1000)
    newAudioVid4 = VidTrim(dvidtrack, newAudio4Vidlen)

    oufilv4 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeatvid4" + tracknam + str(ctr) + ".mp4"
    newAudioVid4.write_videofile(oufilv4)

    newAudio5 = newAudioc2.overlay(newAudio4)
    newAudio5Vidlen = int(len(newAudio5)/1000)
    newAudioVid5 = VidTrim(cvidtrack2, newAudio5Vidlen)

    oufilv5 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeatvid5" + tracknam + str(ctr) + ".mp4"
    newAudioVid5.write_videofile(oufilv5)

    newAudio6 = newAudioc.overlay(newAudio5)
    newAudio6Vidlen = int(len(newAudio6)/1000)
    newAudioVid6 = VidTrim(cvidtrack, newAudio6Vidlen)

    oufilv6 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeatvid6" + tracknam + str(ctr) + ".mp4"
    newAudioVid6.write_videofile(oufilv6)

    newAudio7 = newAudiob.overlay(newAudio6)
    newAudio7Vidlen = int(len(newAudio7)/1000)
    newAudioVid7 = VidTrim(bvidtrack, newAudio6Vidlen)

    oufilv7 = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\newsamplebeatvid7" + tracknam + str(ctr) + ".mp4"
    newAudioVid7.write_videofile(oufilv7)

    newAudio8 = newAudio.overlay(newAudio7)
    newAudio8Vidlen = int(len(newAudio8)/1000)
    newAudioVid8 = VidTrim(avidtrack, newAudio8Vidlen)

    oufilv8 = "C:\\Users\\mysti\\CDesktop\\AutoProd\\VidOutput\\newsamplebeatvid8" + tracknam + str(ctr) + ".mp4"
    newAudioVid8.write_videofile(oufilv8)

    newAudio9 = PyPlanker(newAudio8)
    newAudio9Vidlen = int(len(newAudio9)/1000)
    newAudioVid9 = VidTrim(avidtrack, newAudio9Vidlen)

    oufilv9 = "C:\\Users\\mysti\\CDesktop\\AutoProd\\VidOutput\\newsamplebeatvid9" + tracknam + str(ctr) + ".mp4"
    newAudioVid9.write_videofile(oufilv9)

    newAudiopp = newAudio9 * 4
    newAudioppVidlen = int(len(newAudiopp)/1000)

    #prod = int(360000 / (len(newAudiopp)))

    #rep2 = prod - 3

    #rep = random_number2(rep2, prod)

    #newAudiog = newAudiopp * rep

    newAudiopp = newAudiopp - 2

    oufil = "C:\\Users\\mysti\\Desktop\\AutoProd\\VidOutput\\newsamplebeat" + "_" + tim + "_" + str(ctr) + ".wav"

    newAudiopp.export(oufil, format="wav")
    
    #except:
        #print("File unreadable.")  

#call(["python", "NuDubber121.py"])

#call(["python", "VidMixPart3.py"])

## THE GHOST OF THE SHADOW ##