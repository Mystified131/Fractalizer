#This code imports the necessary modules.

import shutil
import os

srchstr = "H:\\Visual\\BlackAndWhitePhotography"

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file       
                         
        content.append(filepath)

        print(filepath)

conlen = len(content) - 1

for ctr in range(conlen, 0, -1):

    outstr = 'C:\\Users\\mysti\\Coding\\Fractalizer\\' + str(ctr) + ".jpg"
    shutil.copy(content[ctr], outstr)

## THE GHOST OF THE SHADOW ##


