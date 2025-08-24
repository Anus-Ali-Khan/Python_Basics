# import whole module use as to give shorter name
# this method used to import module from same directory
import my_module as mm

# We can import whole functions of module at once by using * but this will create problems in tracking error
# from my_module import *

# for directly importing the d=specified function from module
from my_module import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses,'Math') # call function by importing module
index2 = fi(courses,'Physics') # directly imported the function
print(index)
print(index2)
print(test)


# when we import module python lokks in the sys directories list
import sys
print(sys.path)

# If a module is another dirctory
#  1st Method: add that directory in sys list

sys.path.append('d:\\Anus(Coding)\\AI')

# 2nd Method: to change environment variable this process is differnt for mac and windows
# For Mac
# In terminal write: nano ~/.bash_profile
# then a script will open at tyhe end of it add 
# export PYTHONPATH="path to new directory" 
# restart the terminal
# type python
# then imort my_module_desktop 

# For Windows 
# Go to advanced System Settings
# Environment VAriables
# Add PYTHONPATH
# Is value path
# save and open cmd the type python and import my_module_desktop(your module name)

# Standard Libraries
import random
import math
import datetime
import calendar
import os

print(os.getcwd()) # gives current directory
print(os.__file__) # gives the location of library
