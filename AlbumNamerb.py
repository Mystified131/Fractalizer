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
from TextGetter import GetWebText

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

srchstr = 'C:\\Users\\mysti\\Coding\\Fractalizer'

wordcon = GetWebText()

x1 = len(wordcon)

num1 = random_number(x1)
num2 = random_number(x1)
num3 = random_number(x1)
num4 = random_number(x1)
astr = wordcon[num1]
bstr = wordcon[num2]
cstr = wordcon[num3]
dstr = wordcon[num4]
phrsstr = astr.title() + "_" + bstr.title() + "_" + cstr.title()  + "_" + dstr.title()

instr = "H:\\Spirit_Circuits\\NewAlbum"
#instr = "C:\\Users\\mysti\\Desktop\\NewAlbum"

#instr = "C:\\Users\\mysti\\Desktop\\NewAlbum"

outstr = "H:\\Spirit_Circuits\\" + phrsstr
#outstr = "C:\\Users\\mysti\\Desktop\\" + phrsstr

#outstr = "C:\\Users\\mysti\\Desktop\\" + phrsstr

try:

    os.rename(instr, outstr)

except:

    print("")

    print("Unable to rename directory.")

print("")


print("Your project should be ready for you in the AutoProd folder on your desktop and a folder in the Spirit Circuits folder on your Seagate external drive.")


print("")

call(["python", "C:\Users\mysti\Coding\RoboDJ\DJNewBigBad.py"])

## THE GHOST OF THE SHADOW ##
