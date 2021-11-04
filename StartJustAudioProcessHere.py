from subprocess import call
import shutil
import os
from pydub import AudioSegment

print("")

print("This will convert wav files in the Desktop folder 'AutoProd', adding vocel samples and other album accutrements.")

print("")

print("The result will be saved in a folder in your external drive.")

print("")

testfile = "G:\\0.114_997281561._occurrence.wav"

try:
    TestAudio = AudioSegment.from_wav(testfile)  
    astr = "G"

except:
    astr = "H"

fillst = []

for subdir, dirs, files in os.walk("C:\\Users\\mysti\\Desktop\\AutoProd\\Raw"):

    for file in files:
        filepath = subdir + os.sep + file

        if ".wav" in str(filepath):

            fillst.append(filepath)

for elem in fillst:
    ddir = "C:\\Users\\mysti\\Coding\\Fractalizer"

    try:

        shutil.copy(elem, ddir)
        print("Copying Track.")
        print("")

    except:

        print("Track transfer error.")
        print("")

if astr == 'G':

    call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\JustAudioAddSpeakInParagraphsWorldFact.py"])

if astr != 'G':

    call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\JustAudioAddSpeakInParagraphsWorldFactb.py"])


## THE GHOST OF THE SHADOW ##