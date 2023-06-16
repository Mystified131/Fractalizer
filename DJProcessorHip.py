#This code imports the necessary modules.

from pydub import AudioSegment
import random
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

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

contentbeats = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "beat" in str(filepath):
            cline = str(file)
            contentbeats.append(cline)

contentdrones = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "drone" in str(filepath):
            cline = str(file)
            contentdrones.append(cline)

contentperc = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "perc" in str(filepath):
            cline = str(file)
            contentperc.append(cline)

contentpepper = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "pepper" in str(filepath):
            cline = str(file)
            contentpepper.append(cline)

contentbass = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "bass" in str(filepath):
            cline = str(file)
            contentbass.append(cline)

contentorg = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "organ" in str(filepath):
            cline = str(file)
            contentorg.append(cline)

contentsax = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "sax" in str(filepath):
            cline = str(file)
            contentsax.append(cline)

contentgit = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
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

    #try:

    newAudio = AudioSegment.from_wav(atrack)
            

    newAudiob = AudioSegment.from_wav(btrack)

    newAudiob = newAudiob - 4

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

    newAudio2 = newAudioe2.overlay(newAudio1)

    newAudio3 = newAudioe.overlay(newAudio2)

    newAudio4 = newAudiod.overlay(newAudio3)

    newAudio5 = newAudioc2.overlay(newAudio4)

    newAudio6 = newAudioc.overlay(newAudio5)

    newAudio7 = newAudiob.overlay(newAudio6)

    newAudio8 = newAudio.overlay(newAudio7)

    newAudiopp = newAudio8 * 4

    #prod = int(360000 / (len(newAudiopp)))

    #rep2 = prod - 3

    #rep = random_number2(rep2, prod)

    #newAudiog = newAudiopp * rep

    newAudiopp = newAudiopp - 2

    oufil = "C:\\Users\\mysti\\Coding\\Fractalizer\\newsamplebeat" + tracknam + str(ctr) + ".wav"

    #if int(os.stat(newAudiog).st_size) < sizlim:
    newAudiopp.export(oufil, format="wav")
        
    #except:
        #print("File unreadable.")  

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
            stutdic = random_number(10)
            if stutdic > 7:
                newAudio = add_stutter(newAudio)
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
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
            newAudio = newAudio - 5
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\\Fractalizer\\newsampledrone" + tracknam + str(ctr) + ".wav"
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
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
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
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
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
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
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
            delic = random_number(10)
            if delic > 7:
                newAudio = add_deelay(newAudio)
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
            newAudio = newAudio -3
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\\Fractalizer\\newsamplepepper" + tracknam + str(ctr) + ".wav"
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

        stutdic = random_number(10)

        if stutdic > 6:
            newAudio = add_stutter(newAudio)

        sil2 = random_number2(18000,26000)

        back = AudioSegment.silent(duration = sil2)

        newAudio = newAudio -3
        
        newAudio = newAudio + back
        
        oufil = "C:\\Users\\mysti\\Coding\\Fractalizer\\newsampleguitar" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

#call(["python", "NuDubber121.py"])

call(["python", "NuDubberHipHop.py"])

## THE GHOST OF THE SHADOW ##