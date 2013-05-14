#-*- coding: utf-8 -*-

import base64
import os, os.path
import sys
import cmd
import time

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

class cmd_input(cmd.Cmd):
  #local time - get h:min:sec
  localtime_h = time.localtime()[3]
  localtime_m = time.localtime()[4]
  localtime_s = time.localtime()[5]  
  prompt = str(localtime_h)+':'+str(localtime_m)+':'+str(localtime_s)+' λ.春: '
  def do_sysinfo(self,line):
    print '[ ' + os.name + ' ' + sys.platform + ' ]'
    print os.uname()
  def do_count_files(self,line):
    print len([name for name in os.listdir('.') if os.path.isfile(name)])
  def do_quit(self,line):
    sys.exit("sayonara")

if __name__ == '__main__':
  #~localtime - notes /how to call ~#
  #tm_year = str(time.localtime()[0])
  #tm_mon  = str(time.localtime()[1])
  #tm_mday = str(time.localtime()[2])
  #tm_hour = str(time.localtime()[3])
  #tm_min  = str(time.localtime()[4])
  cmd_input().cmdloop()
