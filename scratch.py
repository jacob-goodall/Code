from easygui import *
import sys

x  = fileopenbox(msg="open file", title="Select File", multiple=False)
print(x)