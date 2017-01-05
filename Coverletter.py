import easygui as g
import time
import webbrowser


with open('coverLetter.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')
 # imported the unformatted CoverLetter => data

 # start of easygui stuff
msg = "Enter information for cover letter"
title = "Cover letter creator"
fieldNames = ["Job Title","home/school","Company Name"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
    
#end of easygui stuff

words = data.split(" ")
if fieldValues[1] == "home":
    address = "551 Alsace Lorraine \nHalf Moon Bay, Ca 94019"
elif fieldValues[1] == "school":
    address = "165 Berkeley Ave. \nIrvine, Ca 92612"
else:
    address = "165 Berkeley Ave. \nIrvine, Ca 92612"

for i in range (0,len(words)):
    if words[i] == "*Date*":
        words[i] = time.strftime("%x")
    elif words[i] == "*Position*":
        words[i] = fieldValues[0]
    elif words[i] == "*Address*":
        words[i] = address
    elif words[i] == "*Company*":
        words[i] = fieldValues[2]
    elif words[i] == "*Company*.":
        words[i] = fieldValues[2] + "."
            
filename = fieldValues[2] + "_coverletter.txt"
f = open(filename,'w')
for i in range(0,len(words)):
    f.write(words[i])
    f.write(" ")
    if i < 7 and i != 1 or words[i] == "experience." or words[i] == "position.":
        f.write("\n")
f.close()

webbrowser.open(filename)
    
