import random
import os
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call
import cv2
import numpy as np

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

#Imgpt = "F:\\Visual\\VisualArt"

#Imgpt = "F:\\Visual\\VariousImages\\Polaroid\PolArt"

try:

    Imgpt = "F:\\PolArt"

except:

    Imgpt = "E:\\PolArt"

contentgraph = []

for subdir, dirs, files in os.walk(Imgpt):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg") and "lw" in str(filepath):
            contentgraph.append(str(filepath))

plen = len(contentgraph)

numi = 0

for ctr in range(20):

    if numi < 1:

        print("")

        print("Generating Cover Art: " + (str(numi + 1)))
            
        pch = random_number(plen)
        ppt = contentgraph[pch]

        print(ppt)

        m =  cv2.imread(ppt)

        h,w,bpp = np.shape(m)

        a = random_number2(50, 232)
        b = random_number2(50, 232)
        c = random_number2(50, 232)

        bi = np.zeros((999,999,3), np.uint8)

        try: 
            
            for py in range(0,999):
                for px in range(0,999):
            #can change the below logic of rgb according to requirements. In this 
            #white background is changed to #e8e8e8  corresponding to 232,232,232 
            #intensity, red color of the image is retained.
                    #f(m[py][px][0] >200): 
                        
                    bi[py][px][0] =  m[py][px][0] + a
                    bi[py][px][1] =  m[py][px][1] + b
                    bi[py][px][2] =  m[py][px][2] + c

                
            outpath = "G:\\NewBadBeats\\NewAlbum\\ZZZ_Cover_" + str(tim) + str(numi) +".jpg"

            #cv2.imshow('matrix', bi)
            #cv2.waitKey(0)
            cv2.imwrite(outpath, bi)

            numi += 1

        except:
            print("")
            print("Image too small.")
            print("")

print("")

print("Images created and saved in the output folder.")

print("")

call(["python", "C:\\Users\\mysti\\Coding\\Fractalizer\\LinerNotes.py"])

## THE GHOST OF THE SHADOW ##



