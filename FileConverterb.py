import soundfile as sf
from subprocess import call
import os

contentoggs = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".ogg") and "Generated" in str(filepath):
            contentoggs.append(str(file))

print("")
print("Converting from ogg to wav")
print("")

ctr = 0

for elem in contentoggs:

    try:
        ctr += 1
        data, samplerate = sf.read(elem)
        outstr = "C:\\Users\\mysti\\Coding\\Fractalizer\\Generated_voxraw_" + str(ctr) + ".wav" 
        sf.write(outstr, data, samplerate)

    except:
        print("")
        print("File conversion error.")

call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\NuDubVoxSonb.py"])

## THE GHOST OF THE SHADOW ##