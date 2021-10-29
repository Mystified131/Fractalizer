from subprocess import call
import shutil
import os

print("")

print("This will convert wav files in the Desktop folder 'AutoProd', adding vocel samples and other album accutrements.")

print("")

print("The result will be saved in a folder in your external drive.")

print("")

#astr = input("Enter 'G' if your Seagate Portable is at that location, or enter 'H' otherwise: ")

astr = "H"

fillst = []

for subdir, dirs, files in os.walk('"C:\\Users\\mysti\\Desktop\\AutoProd\\Raw"'):

    for file in files:
        filepath = subdir + os.sep + file

        if ".wav" and "Track" in str(filepath):

            fillst.append(filepath)

for elem in fillst:
    ddir = "C:\\Users\\mysti\\Coding\\Fractalizer"
    shutil.copy(elem, ddir)

if astr == 'G':

    call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\SpeakInParagraphsWorldFact.py"])

if astr != 'G':

    call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\SpeakInParagraphsWorldFactb.py"])


## THE GHOST OF THE SHADOW ##