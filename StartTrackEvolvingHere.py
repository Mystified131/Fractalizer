from subprocess import call

print("")

print("This will convert wav files in the local folder with 'Track' in their name, adding vocel samples and other album accutrements.")

print("")

print("The result will be saved in a folder in your external drive.")

print("")

astr = input("Enter 'G' if your Seagate Portable is at that location, or enter 'H' otehrwise: ")

if astr == 'G':

    call(["python", "SpeakInParagraphsWorldFact.py"])

if astr != 'G':

    call(["python", "SpeakInParagraphsWorldFactb.py"])


## THE GHOST OF THE SHADOW ##