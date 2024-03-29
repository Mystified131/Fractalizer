import soundfile as sf
from subprocess import call
import os
import shutil
import datetime
import soundfile as sf


def bitratetoredbook(filepath, outpath):

    # Read wav with default
    #fn_wav = os.path.join('..', 'data', 'B', 'FMP_B_Note-C4_Piano.wav')
    x, Fs = sf.read(filepath)
    outpath(x=x,Fs=Fs,text='WAV file (default): ')

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

contentops = []

#srstr = "F:\\OriginalAudio\\Sounds\\Acid_Loops\\NewSound"

srstr = "E:\\Acid_Loops\\NewSound"

for subdir, dirs, files in os.walk(srstr):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith('.wav'):

            contentops.append(str(filepath))

tlen = len(contentops)

for ctr in range(tlen):

    elem = contentops[ctr]

    ofstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\GenCh_' + str(ctr) + '_' + str(tim) + '.wav'

    shutil.copy(elem, ofstr)

contentoggs = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".ogg") and "Generated" in str(filepath):
            contentoggs.append(str(filepath))

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

call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\NuDubVoxSon.py"])

## THE GHOST OF THE SHADOW ##