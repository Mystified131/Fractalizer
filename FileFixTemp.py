import os

srchstr = "C:\\Users\mysti\\Desktop\\zips\\unzipped"

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
        
        #if  filepath.endswith(".wav") and( ("Jazz" in filepath) and (("Drum" not  in filepath)) and ("Beat" not  in filepath) and  ("Bass" not  in filepath))  :  
        #if  filepath.endswith(".wav") and ("Min" in str(filepath)) or (("Synth" in str(filepath)) and ("Analog" in str(filepath))) and   (("Beat" not in str(filepath)) and ("Drum" not in str(filepath)) and ("Bass" not in str(filepath))) :                          
        #if  filepath.endswith(".wav") and (("Chant" in filepath) or  ("HomeLoops2022" in filepath)) and  (("Pad"in filepath) or ("Strings" in filepath)):  
        if  "(1).jpg" in filepath:

            os.remove(filepath)

            #"C:\Users\mysti\Desktop\zips\unzipped\VariousOnlneAIGeneratedImages-20221022T085524Z\VariousOnlneAIGeneratedImages\2arYJ0j2GlBbeB5FLoCu--1--MR2UP_6x (1).jpg"
                         
print("")

print("All necessary files removed.")

print("")