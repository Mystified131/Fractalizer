from subprocess import call

print("")

astr = input("Press 's' to use scrambled text, or press 'enter' otehrwise: ")

if astr == 's':

    call(["python", "SpeakInParagraphsWorldFact.py"])

if astr != 's':

    call(["python", "TextToSpeechWorld.py"])


## THE GHOST OF THE SHADOW ##