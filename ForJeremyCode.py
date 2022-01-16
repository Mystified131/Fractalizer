##PART 1: Gathering Sounds

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

srchstr = 'E:\\OriginalAudio\\Sounds\\Acid_Loops'

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
        
        if  filepath.endswith(".wav")  and ("ZZ Indie" not in str(filepath)) and (("Glitch" in str(filepath)) or ("House" in str(filepath))) :  

            contentbeats.append(filepath)
             
            contentsax.append(filepath)

            contentgit.append(filepath)
             
            contentpepper.append(filepath)
               
            contentdrones.append(filepath)

            contentperc.append(filepath)

            contentorg.append(filepath)

            contentbass.append(filepath)
        
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

call(["python", "DJProcessorNuFlyTrac.py"])

## THE GHOST OF THE SHADOW ##

##PART 2: Selecting Sounds

#This code imports the necessary modules.

from pydub import AudioSegment
import random
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

contentbeats = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "beat" in str(filepath):
            cline = str(file)
            contentbeats.append(cline)

contentdrones = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "drone" in str(filepath):
            cline = str(file)
            contentdrones.append(cline)

contentperc = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "perc" in str(filepath):
            cline = str(file)
            contentperc.append(cline)

contentpepper = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "pepper" in str(filepath):
            cline = str(file)
            contentpepper.append(cline)

contentbass = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "bass" in str(filepath):
            cline = str(file)
            contentbass.append(cline)

contentorg = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "organ" in str(filepath):
            cline = str(file)
            contentorg.append(cline)

contentsax = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "sax" in str(filepath):
            cline = str(file)
            contentsax.append(cline)

contentgit = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "guitar" in str(filepath):
            cline = str(file)
            contentgit.append(cline)

print("Extracting samples. Please wait.")

print("")

sizlim = 15000000

for ctr in range(50):

    astr = ("Beat Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentbeats))
    atrack = contentbeats[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    bstr = ("Bass Sample: " + str(ctr + 1))
    print(bstr)
        
    songchb = random_number2(0,len(contentbass))
    btrack = contentbass[songchb]


    cstr = ("Organ Sample: " + str(ctr + 1))
    print(cstr)
        
    songchc = random_number2(0,len(contentorg))
    songchc2 = random_number2(0,len(contentdrones))

    det = random_number(2)
    if det == 0:
        ctrack = contentorg[songchc]      
    if det == 1:
        ctrack = contentdrones[songchc2] 

    cstr = ("Organ Sample 2: " + str(ctr + 1))
    print(cstr)
        
    songchc = random_number2(0,len(contentorg))
    songchc2 = random_number2(0,len(contentdrones))

    det = random_number(2)
    if det == 0:
        ctrack2 = contentorg[songchc]      
    if det == 1:
        ctrack2 = contentdrones[songchc2] 

    dstr = ("Stab Sample: " + str(ctr + 1))
    print(dstr)
        
    songchd = random_number2(0,len(contentsax))
    dtrack = contentsax[songchd]   

    estr = ("Perc Sample: " + str(ctr + 1))
    print(estr)
        
    songche = random_number2(0,len(contentperc))
    etrack = contentperc[songche]   

    estr = ("Perc Sample 2: " + str(ctr + 1))
    print(estr)
        
    songche = random_number2(0,len(contentperc))
    etrack2 = contentperc[songche]   

    fstr = ("Perc Sample 3: " + str(ctr + 1))
    print(fstr)
        
    songchf = random_number2(0,len(contentperc))
    ftrack = contentperc[songchf] 

    fstr = ("Perc Sample 4: " + str(ctr + 1))
    print(fstr)
        
    songchf = random_number2(0,len(contentperc))
    ftrack2 = contentperc[songchf] 

    if etrack == ftrack:
        try:
            ftrack = contentperc[songchf + 1] 

        except:
            ftrack = contentperc[songchf - 1] 

    try:

        newAudio = AudioSegment.from_wav(atrack)
        
        newvol = random_number2(3,6)
        newAudio = newAudio - newvol
        newAudio = newAudio.fade_in(10)
        newAudio = newAudio.fade_out(10)

        newAudiob = AudioSegment.from_wav(btrack)
        
        #newvolb = random_number2(8,12)
        #newAudiob = newAudiob - newvolb
        newAudiob = newAudiob.fade_in(10)
        newAudiob = newAudiob.fade_out(10)

        if len(newAudio) < len(newAudiob):

            amt = len(newAudio)

            newAudiob = newAudiob[1:amt]

        newAudioc = AudioSegment.from_wav(ctrack)
        
        newvolc = random_number2(12,15)
        newAudioc = newAudioc - newvolc
        if len(newAudio) <= len(newAudioc):
            baulen = len(newAudio)
        if len(newAudio) > len(newAudioc):
            baulen = len(newAudioc)
        q1 = ((random_number(4) / 10))
        q2 = ((random_number(3) / 10) + q1)
        baulen1 = int(baulen * q1)
        baulen2 = int(baulen * q2)
        newAudioc = newAudioc[baulen1:baulen2]

        if len(newAudio) < len(newAudioc):

            amt = len(newAudio)

            newAudioc = newAudioc[1:amt]

        newAudioc2 = AudioSegment.from_wav(ctrack2)
        
        newvolc = random_number2(12,15)
        newAudioc2 = newAudioc2 - newvolc
        if len(newAudio) <= len(newAudioc2):
            baulen = len(newAudio)
        if len(newAudio) > len(newAudioc2):
            baulen = len(newAudioc)
        baulen = len(newAudio)
        q1 = ((random_number(4) / 10))
        q2 = ((random_number(3) / 10) + q1)
        baulen1 = int(baulen * q1)
        baulen2 = int(baulen * q2)
        newAudioc2 = newAudioc2[baulen1:baulen2]

        if len(newAudio) < len(newAudioc2):

            amt = len(newAudio)

            newAudioc2 = newAudioc2[1:amt]

        newAudiod = AudioSegment.from_wav(dtrack)

        newvold = random_number2(8,12)
        newAudiod = newAudiod - newvold

        if len(newAudio) < len(newAudiod):

            amt = len(newAudio)

            newAudiod = newAudiod[1:amt]

        newAudiod = newAudiod.fade_in(1000)
        newAudiod = newAudiod.fade_out(1000)
      
        newAudioe = AudioSegment.from_wav(etrack)
        
        newvole = random_number2(10,12)
        newAudioe = newAudioe - newvole
        detl = len(newAudio) / 2
        if len(newAudioe) <= detl:
            newAudioe = newAudioe * 2

        if len(newAudio) < len(newAudioe):

            amt = len(newAudio)

            newAudioe = newAudioe[1:amt]

        newAudioe = newAudioe.fade_in(10)
        newAudioe = newAudioe.fade_out(10)

        newAudioe2 = AudioSegment.from_wav(etrack2)
        
        newvole = random_number2(10,12)
        newAudioe2 = newAudioe2 - newvole
        detl = len(newAudio) / 2
        if len(newAudioe2) <= detl:
            newAudioe2 = newAudioe2 * 2

        if len(newAudio) < len(newAudioe2):

            amt = len(newAudio)

            newAudioe2 = newAudioe2[1:amt]

        newAudioe2 = newAudioe2.fade_in(10)
        newAudioe2 = newAudioe2.fade_out(10)

        newAudiof = AudioSegment.from_wav(ftrack)
        
        newvolf = random_number2(12, 14)
        newAudiof = newAudiof - newvolf
        detl = len(newAudio) / 2
        if len(newAudiof) <= detl:
            newAudiof = newAudiof * 2

        if len(newAudio) < len(newAudiof):

            amt = len(newAudio)

            newAudiof= newAudiof[1:amt]

        newAudiof = newAudiof.fade_in(10)
        newAudiof = newAudiof.fade_out(10)

        newAudiof2 = AudioSegment.from_wav(ftrack2)
        
        newvolf = random_number2(12, 14)
        newAudiof2 = newAudiof2 - newvolf
        detl = len(newAudio) / 2
        if len(newAudiof2) <= detl:
            newAudiof2 = newAudiof2 * 2

        if len(newAudio) < len(newAudiof2):

            amt = len(newAudio)

            newAudiof2= newAudiof2[1:amt]

        ewAudiof2 = newAudiof2.fade_in(10)
        newAudiof2 = newAudiof2.fade_out(10)

        newAudiov = newAudiob.overlay(newAudio)

        newAudiof = newAudiof.overlay(newAudiov)

        newAudioe = newAudioe.overlay(newAudiof)

        newAudioz = newAudioc.overlay(newAudioe)

        newAudiof2 = newAudiof2.overlay(newAudiov)

        newAudioe2 = newAudioe2.overlay(newAudiof2)

        newAudioz2 = newAudioc2.overlay(newAudioe2)

        newAudiodd = newAudiod * 4
        
        #det = random_number(3)

        #if det == 0:
        newAudioqq = newAudioz + newAudiov + newAudioz2 + newAudiov + newAudiov + newAudioz2 + newAudiov + newAudioz2 + newAudioz2 + newAudioz + newAudiov + newAudiov + newAudioz2 + newAudioz + newAudiov + newAudiov

        newAudiopp = newAudiodd.overlay(newAudioqq)

        prod = int(360000 / (len(newAudiopp)))

        rep2 = prod - 3

        rep = random_number2(rep2, prod)

        newAudiog = newAudiopp * rep

        newAudiog = newAudiog - 2

        oufil = "C:\\Users\\mysti\\Coding\Fractalizer\\newsamplebeat" + tracknam + str(ctr) + ".wav"

        #if int(os.stat(newAudiog).st_size) < sizlim:
        newAudiog.export(oufil, format="wav")
        
    except:
        print("File unreadable.")  

print("Overlaying recording.")

for ctr in range(50):

    astr = ("Drone Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentdrones))
    atrack = contentdrones[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random_number(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(5000, 8000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(14,20)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(100)
            newAudio = newAudio.fade_out(100)
            sil1 = random_number2(12000, 17000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(48000, 53000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(14,17)
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
                samplen = random_number2(40000, 42000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(14,18)
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
                samplen = random_number2(2000, 7000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(14,26)
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
        oufil = "C:\\Users\\mysti\\Coding\Fractalizer\\newsampledrone" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(50):

    astr = ("Other Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentpepper))
    atrack = contentpepper[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random_number(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(1600, 2400)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(8,12)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(4000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(8000, 24000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(12,18)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(12000)
            sil2 = random_number(16000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 7 and solonum < 11:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random_number2(50000, 52000)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(10,14)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(20000)
            sil2 = random_number(22000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 10:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random_number2(200, 800)
                sampst = int(leng - samplen)
                t1 = random_number(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random_number2(10,14)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(10)
            newAudio = newAudio.fade_out(10)
            addAudio = newAudio
            ctr = random_number2(3,8)
            for sam in range(ctr):
                newAudio += addAudio
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random_number(10000)
            sil2 = random_number(14000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back

        dic = random_number(10)
        if dic == 7:
            sil1 = random_number(60000)
            sil2 = random_number(50000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\Fractalizer\\newsamplepepper" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(50):

    astr = ("Guitar Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random_number2(0,len(contentgit))
    atrack = contentgit[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        
        newvol = random_number2(15, 18)
        newAudio = newAudio - newvol
        newAudio = newAudio 
        newAudio = newAudio.fade_in(100)
        newAudio = newAudio.fade_out(100)

        sil2 = random_number2(18000,26000)

        back = AudioSegment.silent(duration = sil2)
        
        newAudio = newAudio + back
        
        oufil = "C:\\Users\\mysti\\Coding\Fractalizer\\newsampleguitar" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

call(["python", "NuDubber.py"])

## THE GHOST OF THE SHADOW ##

##PART 3: Editing Sounds

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

        newAudioamb2 = newAudioamb2 * 8

        newAudiobeat = AudioSegment.from_wav(atrack1) 

        if len(newAudiobeat) >= len(newAudioamb2):

            newAudionear = newAudioamb2.overlay(newAudiobeat)
        
        if len(newAudiobeat) < len(newAudioamb2):

            newAudionear = newAudiobeat.overlay(newAudioamb2)

        newAudionear = newAudionear.fade_in(5000)
        newAudionear = newAudionear.fade_out(15000)
            
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

            oufil = "C:\\Users\\mysti\\Desktop\\AutoProd\\Raw\\Mastered_Track" + tim + "." + str(suctot) + ".wav"
            newAudio3.export(oufil, format="wav")

            suctot += 1

            if suctot == trtot:
                break

    except:

        print("")

        print("Error during render. File not created.")

## THE GHOST OF THE SHADOW ##



