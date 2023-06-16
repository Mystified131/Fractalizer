import turtle
import datetime
import random
import string
from unidecode import unidecode
from RandFunct import random_number
from RandFunct2 import random_number2
import os
from tkinter import *
from subprocess import call
from TextGetter import GetWebText

totlst = GetWebText()

totlen = len(totlst)

#wn = turtle.Screen()

#wn.setup(width = 1.0, height = 1.0)

#These next three lines will create a fullscreen effect but will also not allow an esc exit

#canvas = wn.getcanvas()

#root = canvas.winfo_toplevel()

#root.overrideredirect(1)

collst = ["black", "silver"]

#bcollst = ["light blue", "tan", "white"]

bcollst = ["white", "white", "white"]

stllst = ["normal", "bold", "italic", "underline"]

tommy = turtle.Turtle()

tommy.speed(1000)

for reps in range(1):

    print("")

    print("Rendering GenText Cover Art Option: " + str(reps + 1) + " / " + "3")

    print("")

#for reps in range(10000):

    turtle.clearscreen()

    bkgr = random_number(len(bcollst))

    back = bcollst[bkgr]

    turtle.bgcolor(back)

    #turtle.bgcolor("white")

    #collst.remove(bcollst[bkgr])

    #shnum = random_number2(90, 115)

    #shnum = random_number2(350, 500)

    shnum = 180

    for ctr in range(shnum):

        fgr = random_number(len(collst))

        fore = collst[fgr]

        tommy.color(fore)

        N = random.randrange(12)

        stnum = random_number(totlen)

        stx = totlst[stnum]

        #stx = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

        xco = random_number2(-340, 240)

        yco = random_number2(-300, 300)

        sz = random_number2(12,56)

        stlen = len(stllst)

        styl = random_number(stlen)

        styll = stllst[styl]

        tommy.penup()

        tommy.goto(xco, yco)

        tommy.write(stx, font=("Courier", sz, styll))

    
    #this code retrieves the date and time from the computer, to create the timestamp

    right_now = datetime.datetime.now().isoformat()

    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    ts = turtle.getscreen()

    filnm = 'C:\\Users\\mysti\\Coding\\GenArt_' + tim + ".eps"

    ts.getcanvas().postscript(file=filnm)

turtle.clearscreen()
    
turtle.bye()

#call(["python", "BatchDeleter.py"])

## THE GHOST OF THE SHADOW ##