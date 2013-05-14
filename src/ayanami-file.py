import base64
import os
import sys

print_info = False
type_in = ''

def type_in():
  type_in = raw_input('> ')

def print_info(type_in):
  if type_in == "print info":
    print_info = True
  if print_info == True:
    print os.name 
    print sys.platform
    print os.uname()

if type_in == "quit":
  sys.exit("sayonara~")

while not type_in == "quit":
  type_in()
