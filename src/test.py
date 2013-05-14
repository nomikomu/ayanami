import math
import sys
import shelve
from help import *

# This program is free software; you can redistribute it and #
# /or modify it under the terms of the GNU General  Public - #
# License as published by the Free Software Foundation; eit- #
# her version 2 of the License, or (at your option) any lat- #
# er version.                          Copyright 2013 defm03 #
#                                                            #
#              /     \                                       #
#              vvvvvvv  /|__/|                               #
#                 I   /O,O   |                               #
#                 I /_____   |      /|/|                     #
#                J|/^ ^ ^ \  |    /00  |    _//|             #
#                 |^ ^ ^ ^ |W|   |/^^\ |   /oo |             #
#                  \m___m__|_|    \m_m_|   \mm_|             #
#                                                            #
#   NERV HQ - defm03 // github@defm03 // yutsuro@gmail.com   #

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
  if not hasattr(stream, "isatty"):
    return False
  if not stream.isatty():
    return False # auto color only on TTYs
  try:
    import curses
    curses.setupterm()
    return curses.tigetnum("colors") > 2
  except:
    # guess false in case of error
    return False
has_colours = has_colours(sys.stdout)

def printout(text, colour=WHITE):
  if has_colours:
    seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
    sys.stdout.write(seq)
  else:
    sys.stdout.write(text)

printout("[debug]   ", GREEN)
print("in green")

do = 1
class REGISTER:
  def __init__(self,type_o=''):
  	self.type = type_o
  def REGISTER_count(self,intg):
  	self.intg = intg


if input_char = 'p':
  while do == 1:
    intg += 1
    a = REGISTER('A')
    a.REGISTER_count
    if intg < 10:
      print 'REGISTER.EVANGELION ' + 'BLOCK:' + type_o + ' [00x0000' + str(intg) + ']'
    elif intg > 10 and intg < 100:
      print 'REGISTER.EVANGELION ' + 'BLOCK:' + type_o + ' [00x000' + str(intg) + ']'
    elif intg > 100 and intg < 1000:
      print 'REGISTER.EVANGELION ' + 'BLOCK:' + type_o + ' [00x00' + str(intg) + ']'
    elif intg > 1000 and intg < 10000:
      print 'REGISTER.EVANGELION ' + 'BLOCK:' + type_o + ' [00x0' + str(intg) + ']'
    elif intg > 10000 and intg < 100000:
      print 'REGISTER.EVANGELION ' + 'BLOCK:' + type_o + ' [00x' + str(intg) + ']'


list_a = ['4445','6844','4568','4445','6844','4568','4400','0000']
list_b = ['002b','b338','0246','002b','b339','1a46','002b','4568']
def save_reg():
  file = shelve.open('REGISTER_EVA', 'e')
  file['x'] = x
  file.close()
def load_reg():
  global x
  file = shelve.open('REGISTER_EVA', 'r')
  x = file['x']
  file.close()
