#This code imports the necessary modules.

import os

print("")

print("Counting. . . please wait one moment.")

contentsamps = []

for subdir, dirs, files in os.walk('E:\\OriginalAudio\\Sounds\\Acid_Loops'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav") or filepath.endswith(".ogg"))  and ("ZZ Indie" not in str(filepath)):
            cline = str(filepath)
            contentsamps.append(cline)

totlen = len(contentsamps)

print("")

print("Counting. . . please wait one moment.")

print("")

print("Total WAV files in Samples folder, without Indie: ", totlen)

print("")


## THE GHOST OF THE SHADOW ##