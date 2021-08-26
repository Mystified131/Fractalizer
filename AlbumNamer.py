#This code imports the necessary modules.

import os
from RandFunct import random_number
from RandFunct2 import random_number2
import datetime
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import boto3
from subprocess import call

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

srchstr = 'C:\\Users\\mysti\\Coding\\Fractalizer'

content =[]

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".txt"): 
            astr = str(file)
            content.append(astr)

texcon = []

for elem in content:

    infile = open(elem, "r")

    try:
        aline = infile.readline()

    except:

        aline = "null"
    
    while aline:
        try:
            texcon.append(aline)
            aline = infile.readline()
        except: print("Text error-- passing over line.")

    infile.close()

wordcon = []

for elem in texcon:
    al = elem.split()
    for x in al:
        addstr = ""
        for xlet in x:
            if xlet.isalnum() and not xlet.isnumeric():
                addstr += xlet
        xl = addstr.strip()
        xl2 = xl.lower()
        if len(xl2) > 1:
            wordcon.append(xl2)
            
x1 = len(wordcon)

num1 = random_number(x1)
num2 = random_number(x1)
num3 = random_number(x1)
astr = wordcon[num1]
bstr = wordcon[num2]
cstr = wordcon[num3]
phrsstr = astr.title() + "_" + bstr.title() + "_" + cstr.title()

outstr = "E:\\Spirit_Circuits\\" + phrsstr

try:

    os.rename("E:\\Spirit_Circuits\\NewAlbum", outstr)

except:

    print("")

    print("Unable to rename directory.")

print("")

print("Your project should be ready for you in the AutoProd folder on your desktop.")

print("")

call(["python", "BigDreamMachine.py"])

## THE GHOST OF THE SHADOW ##
