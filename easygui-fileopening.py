from easygui import *
import sys
def first():
  filepath  = fileopenbox(title="Select File", multiple=False)
  print(filepath)
  f = open(filepath,'r')
  message = f.read()
  with open(filepath) as a:
      lines = a.readlines()
  new_list = [s.replace("\n", "") for s in lines]
  sorted_new_list = sorted(new_list)

  f.close()
  file = open(filepath,"r")
  Counter = 0

  # Reading from file
  Content = file.read()
  CoList = Content.split("\n")
  for i in CoList:
      if i:
          Counter += 1

  print("Number of People in List:",Counter)
  print(sorted_new_list)
  second()
  12
def second():
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







first()