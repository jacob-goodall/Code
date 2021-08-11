from easygui import *
import sys
#from __future__ import print_function
msg = "Enter Info about task"
title = "Cross Plotter"
fieldNames = ["Width Of Area", "Length of Area", "Amount of people to plot"]
fieldValues = multenterbox(msg, title, fieldNames)
if fieldValues is None:
    #need to make it restart
    sys.exit(0)
# make sure that none of the fields were left blank
while 1:
    errmsg = ""
    for i, name in enumerate(fieldNames):
        if fieldValues[i].strip() == "":
          errmsg += "{} is a required field.\n\n".format(name)
    if errmsg == "":
        break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    if fieldValues is None:
        break
print(fieldValues)