import random
import os
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call
import cv2
import numpy as np
from PIL import Image

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    dimen = 0
    if width >= height:
        dimen = height
    if width < height:
        dimen = width
    return dimen

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

#Imgpt = "C:\\Users\\mysti\\Desktop\\Linn"

Imgpt = "C:\\Users\\mysti\\Coding\\Fractalizer"

contentgraph = []

for subdir, dirs, files in os.walk(Imgpt):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".png"):
            contentgraph.append(str(filepath))

plen = len(contentgraph)

numi = 0

for ctr in range(20):

    if numi < 20:

        print("")

        print("Generating Cover Art: " + (str(numi + 1)))
            
        pch = random_number(plen)
        ppt = contentgraph[pch]

        sizt = get_num_pixels(ppt)

        print(ppt)

        print(sizt)

        m =  cv2.imread(ppt)

        h,w,bpp = np.shape(m)

        a = random_number2(50, 232)
        b = random_number2(50, 232)
        c = random_number2(50, 232)

        bi = np.zeros((sizt, sizt, 3), np.uint8)

        try: 
            
            for py in range(0, sizt):
                for px in range(0, sizt):
            #can change the below logic of rgb according to requirements. In this 
            #white background is changed to #e8e8e8  corresponding to 232,232,232 
            #intensity, red color of the image is retained.
                    #f(m[py][px][0] >200): 
                        
                    bi[py][px][0] =  m[py][px][0] + a
                    bi[py][px][1] =  m[py][px][1] + b
                    bi[py][px][2] =  m[py][px][2] + c

                
            outpath =  "C:\\Users\\mysti\\Coding\\Fractalizer\\Colrize_" + str(tim) + str(numi) +".jpg"
           
    
            #cv2.imshow('matrix', bi)
            #cv2.waitKey(0)
            cv2.imwrite(outpath, bi)

            numi += 1

        except:
            print("")
            print("Image error.")
            print("")

print("")

print("Images created and saved in the output folder.")

print("")

call(["python", "Image_Collage_Ran.py"])

## THE GHOST OF THE SHADOW ##



