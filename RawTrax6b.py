#This code imports the necessary modules

import os
import re
import collections
import operator
from subprocess import call
 
for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\Fractalizer'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".ogg")) or (filepath.endswith(".wav")) or (filepath.endswith(".txt"))  and ("Generate" in str(filepath)) or ("vsamp" in str(filepath)):
            os. remove(filepath) 

print("")

print("The designated files have been removed. Thank you.")

print("")

call(["python", "RawTrax7b.py"])

## THE GHOST OF THE SHADOW ##