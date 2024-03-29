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
#from TextGetter import GetWebText

srchstr = 'C:\\Users\\mysti\\Coding\\Fractalizer'

contentfil = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt") and "Liner" in str(filepath):
            contentfil.append(filepath)

cont = len(contentfil)

for cot in range(cont):

    right_now = datetime.datetime.now().isoformat()          
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    filestr = contentfil[cot]

    #filestr = "Paranoimia2.txt"

    infile = open(filestr, "r")

    contentwords = []

    plist = infile.readline()
    while plist:
        contentwords.append(plist.strip())
        plist = infile.readline()

    infile.close()

    print(contentwords)

    #totstr = ""

    #for elem in contentwords:
        #totstr += (elem + "")

    #senlst = totstr.split('.')

    phrslst = []
        
    #x1 = len(senlst)

    senstr = ",, "

    for elem in contentwords:
        elem3 = elem.split()
        for elem2 in elem3:
            
            #texch = random_number(10)
            texch = 8
            if texch < 6 and len(elem2) > 7:
                astr = elem2[:4]
                for rep in range(random_number2(1,5)):
                    bstr = astr * rep   
                senstr += (bstr + elem2)
            if texch > 5 or len(elem2) < 8:
                senstr += elem2

            senstr += "  "

        senstr += ",, "

    if len(phrslst) < 5:

        phrslst.append(senstr)

    print(phrslst)

    print("")

    outst = ""

    for elemm in phrslst:
        outst += elemm

    for citr in range(1):

        paragraph = ""

        speaktex = ""

        print("Cycle: " + str(cot+1))

        print("")

        right_now = datetime.datetime.now().isoformat()          
        list = []

        for i in right_now:
            if i.isnumeric():
                list.append(i)

        tim = ("".join(list))

        accessKey = ""
        secretKey = ""

        infile = open("asckey.m3u", "r")

        aline = infile.readline()  

        while aline:
            try:
                accessKey += (aline)
                aline = infile.readline()
            except: 
                print("Text error-- passing over line.")

        accessKey = accessKey[20:41].strip()

        infile.close()

        infile = open("datatex.m3u", "r")

        aline = infile.readline()  

        while aline:
            try:
                secretKey += (aline)
                aline = infile.readline()
            except: 
                print("Text error-- passing over line.")

        secretKey = secretKey[37:77].strip()

        infile.close()

        polly = boto3.Session(
                        aws_access_key_id= accessKey,                     
            aws_secret_access_key= secretKey,
            region_name='us-west-2').client('polly')

        #vox = random_number(2)

        #voxlst = ["Joanna", "Matthew", "Vitória", "Léa",  "Takumi", "Zhiyu", "Penélope" ]

        #voxlst = ['Nicole', 'Kevin', 'Enrique', 'Tatyana', 'Russell', 'Olivia', 'Lotte', 'Geraint', 'Carmen', 'Mads', 'Penelope', 'Mia', 'Joanna', 'Matthew', 'Brian', 'Seoyeon', 'Ruben', 'Ricardo', 'Maxim', 'Lea', 'Giorgio', 'Carla', 'Naja', 'Maja', 'Astrid', 'Ivy', 'Kimberly', 'Chantal', 'Amy', 'Vicki', 'Marlene', 'Ewa', 'Conchita', 'Camila', 'Karl', 'Zeina', 'Miguel', 'Mathieu', 'Justin', 'Lucia', 'Jacek', 'Bianca', 'Takumi', 'Ines', 'Gwyneth', 'Cristiano', 'Mizuki', 'Celine', 'Zhiyu', 'Jan', 'Liv', 'Joey', 'Raveena', 'Filiz', 'Dora', 'Salli', 'Aditi', 'Vitoria', 'Emma', 'Lupe', 'Hans', 'Kendra', 'Gabrielle']

        #voxlst = ['Carla', 'Emma', 'Raveena', 'Marlene', 'Mathieu', 'Nicole']

        #voxlst = ['Russell']

        #voxlst = ['Joanna']

        voxlst = ['Brian']

        voxch = random_number(len(voxlst))

        voxstr = voxlst[voxch]

        outaud = "GeneratedAudioMix_" + voxstr +  "_" + tim + ".mp3"

        speaktex = outst

        try:
        # Request speech synthesis
            response = polly.synthesize_speech(Text=speaktex, OutputFormat="mp3",
                                            VoiceId=voxstr)
        #except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
            #print(error)
            #sys.exit(-1)

        #try:
            # Access the audio stream from the response
            # if "AudioStream" in response:
                # Note: Closing the stream is important because the service throttles on the
                # number of parallel connections. Here we are using contextlib.closing to
                # ensure the close method of the stream object will be called automatically
                # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                #output = os.path.join(gettempdir(), outaud)
                output = ("C:\\Users\\mysti\\Coding\\Fractalizer\\" +  outaud)

            #try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())

        except:
            # Could not write to file, exit gracefully
            #print(error)
                    #sys.exit(-1)

            print("")
            print("Error processing speech.")
            print("")

        #else:
            # The response didn't contain audio data, exit gracefully
            #print("")
            #print("Could not stream audio")
            #print("")
            #sys.exit(-1)

        # Play the audio using the platform's default player
        #if sys.platform == "win32":
            #os.startfile(output)
        #else:
            # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
            #opener = "open" if sys.platform == "darwin" else "xdg-open"
            #subprocess.call([opener, output])

print("")
print("Your spoken audio has been generated.")
print("")

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt") and "Liner" in str(filepath):
            #os.remove(filepath)
            print("Goodbye.")

#call(["python", "RockGibBulk.py"])

    ## THE GHOST OF THE SHADOW ##

