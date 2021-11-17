import numpy as np
import PIL
from PIL import Image
import os
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime

def horizontal_set(ilist):
    imgs  = [ PIL.Image.open(i) for i in ilist ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    try:       
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        imgs_comb = PIL.Image.fromarray( imgs_comb)
        return(imgs_comb)
    except:
        print("Collage error.")

def vertical_set(ilist):
    imgs  = [ PIL.Image.open(i) for i in ilist ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    try:
        imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        imgs_comb = PIL.Image.fromarray( imgs_comb)
        return(imgs_comb)
    except:
        print("Collage error.")

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

imlist = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".jpg")) and "Colrize_" in str(filepath):
            imlist.append(filepath)

print("")
print(imlist)

timlen = len(imlist)

print("")
print("Generating Collages.")

for op in range(24):

    print("")
    print("HorzCollage: " + str(op + 1))

    ilist = []

    rt = random_number2(2, 4)

    for ctr in range(rt):

        for smst in range(2):
            imnum = random_number(timlen)
            chsimg = imlist[imnum]
            ilist.append(chsimg)

        finalimg = horizontal_set(ilist)

    outpth = "HCollage_" + str(tim) + "_" + str(op) + ".jpg"
    finalimg.save( outpth ) 

horzlist = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".jpg")) and "HCollage" in str(filepath):
            horzlist.append(filepath)

horzlen = len(horzlist)

print("")

print(horzlist)

for bop in range(24):

    print("")
    print("VertCollage: " + str(bop + 1))

    vilist = []

    rtv = random_number2(2,6)

    for ctrv in range(rtv):

        for vset in range(rtv):
            vimnum = random_number(horzlen)
            chosimg = horzlist[vimnum]
            vilist.append(chosimg)

        totimg = vertical_set(vilist)

    outpth2 = "FourCollage_" + str(tim) + "_" + str(bop) + ".jpg"
    totimg.save( outpth2 ) 

print("")
print("Operation complete. Find images in code folder.")
print("")

## THE GHOST OF THE SHADOW ##
    